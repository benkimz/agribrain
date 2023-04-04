import re
import random
import json
import asyncio
import websockets

async def toy_demo(websocket):
    req = json.loads(await websocket.recv())
    message = req["message"]
    query_id = req["query_id"]
    message = re.sub(r"\s+", " ", message.strip())
    message = re.sub(r"\W+", " ", message)
    print(message)
    message = [item.strip() for item in message.lower().split()]
    print(message)
    if "hi" in message or "hello" in message or "hey" in message:
        toy_reps = [
            #"Hi [SEP]too", 
            "Hey[SEP], [SEP]there", 
            #"Hello[SEP] [SEP]too", 
            "Hey[SEP], [SEP]how[SEP] are [SEP]you?", 
            "Hi[SEP],[SEP] how [SEP]may [SEP]I [SEP]help [SEP]you?"
        ]
        await websocket.send(json.dumps({
            "query_id": query_id, 
            "reply": toy_reps[random.randint(0, len(toy_reps) - 1)]
        }))
    elif "tomatoes" in message:
        await websocket.send(json.dumps({
            "query_id": query_id, 
            "reply": """
                <h5>Planting Tomatoes</h5> [SEP]
                    Tomato [SEP] (Lycopersicon esculentum) [SEP]can be grown throughout the year. 
                    You can start harvesting tomato fruits[SEP] <mark>8 - 9 weeks</mark> after 
                    transplanting. [SEP] One tomato plant can yield[SEP]<mark> 4 - 6 kg (10 - 15 lbs.) 
                    [SEP]of fruits. [SEP]
                <table class="demo table table-hover table-striped table-condensed">
                    <caption style="text-align: center;">weather forecast: temperature</caption>
                    <tr><td>daily mean temp</td><td>change in 8 weeks</td></tr>
                    <tr><td style="color: #006a08;"><b>21 C</b></td>
                        <td style="color: red;"><b>-3 C</b></td></tr>
                </table> [SEP]
                <table class="demo table table-hover table-striped table-condensed">
                    <caption style="text-align: center;">weather forecast: precipitation</caption>
                    <tr><td>daily mean rainfall</td><td>change in 8 weeks</td></tr>
                    <tr><td style="color: #006a08;"><b>18 mm</b></td>
                        <td style="color: #006a08;"><b>+5 mm</b></td></tr>
                </table> [SEP]
                <p>
                    Tomatoes can perform well in temperatures between 20 - 25 C, and medium daily 
                    rainfall of between 18 - 24 mm. It is possible for you to plant at this time.
                </p> [SEP]
                <h6>Land  preparation:</h6> [SEP]
                    <li> 
                        If planting in the ground, loosen the soil using a 
                        garden fork to encourage drainage and aeration.                  
                        Remove all stumps and large stones. Make drains  
                        to remove excess water from the garden if   
                        needed. 
                    </li> [SEP]
                <h6>Mixed cropping: </h6> [SEP]
                    <li>
                        Tomato can be interplanted  with other crops 
                        in the home garden. Allow 0.5 m2 (5 feet2) per 
                        tomato plant. 
                    </li> [SEP]
                <h6> Note: <h6> [SEP]
                    <p class="text-warning">
                        Too  much  water  in  the  soil  will  kill  the  plants 
                        and encourages disease.  
                    </p> [SEP]
                <h6>Container preparation:</h6> [SEP]
                    <li> 
                        If planting in containers, use a container at least 
                        45 cm  (18 inches) by 40 cm (16 inches) and 30 
                        cm (12 inches) deep.
                    </li> [SEP]
                <h6>Transplanting:</h6> [SEP]
                    <li>
                        Transplant  healthy  seedlings 
                        afternoon (3:30 –  4:30 p.m.) when they are  
                        3 - 4 weeks old.
                    </li> [SEP]
                <div style="text-align: center;">
                    Price variation:
                    <img src="./images/price-grp-01.png" alt="phrice grap" height="200">
                </div> [SEP]
                <div><b>Production forecast: </b> <b style="color: #006a08;">2kg/ piece</b></div>
                [SEP]
                <div><b>Production forecast: </b><b style="color: #006a08;">25,000kg/ acre</b></div>                    
                [SEP]                
            """
        }))
        
    elif ("agricultural" in message and "sector" in message) or "agriculture" in message:
        await websocket.send(json.dumps({
            "query_id": query_id, 
            "reply": """
                <h5>{}</h5>
                Agricultural [SEP]sector [SEP]is [SEP]indispensable [SEP]to [SEP]the [SEP]country’s 
                [SEP]economic [SEP]growth, [SEP]food [SEP]security, employment generation and poverty
                alleviation particularly, at the rural level. [SEP]It contributes <mark><b>19.2 </b></mark>[SEP]percent 
                to the [SEP]GDP and provides employment to around <mark><b>38.5</b></mark> percent [SEP]of the 
                labour force. More than [SEP]<mark><b>65-70 </b></mark>[SEP]percent of the population [SEP]
                depends on agriculture [SEP]for its livelihood. [SEP]Agricultural growth rate has been constrained by [SEP]shrinking 
                arable land, climate change, water shortages,[SEP] and large-scale population and labour shift from 
                rural to urban areas. Increasing agricultural [SEP]productivity, therefore, requires adoption 
                of [SEP]new  approaches.  With  strong  forward  and  backward  [SEP]linkages  with  the  
                secondary [SEP](industrial)[SEP] and tertiary [SEP](services) [SEP]sectors, it can play 
                a pivotal role to spur economic growth.[SEP]  However,  this  sector  has  remained [SEP]
                prone  to  several  challenges  like  <u>climate change</u>, variance in [SEP]<u>temperature</u>, 
                [SEP] <u>water shortage</u>, [SEP]and changes in pattern of precipitation[SEP] along with increase in 
                [SEP]input prices[SEP].[SEP]             
            """.format("Agricultural sector:")
        }))
    elif "thankyou" in message:
        await websocket.send(json.dumps({
            "query_id": query_id, 
            "reply": """
            <h6 style='color: #006a08;'>You are welcome. 
            I will be here for further assistance. Have a great day!</h6>
            """
        }))

async def main():
    async with websockets.serve(toy_demo, "localhost", 8765):
        await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())
