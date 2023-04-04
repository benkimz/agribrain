var startDate = "2000-01-01";
var endDate = "2010-01-01";

var scale = 1000;

var dataset_name = "era5_ke_weather_data_from_"+startDate+"_to_"+endDate;

var gaul = ee.FeatureCollection("FAO/GAUL/2015/level2");
var kenyaCounties = gaul.filter(ee.Filter.eq('ADM0_NAME', 'Kenya'));
var getRoiPolygon = function(feature) {
  var geometry = feature.geometry();
  var bbox = geometry.bounds().coordinates().get(0);
  var roiPolygon = ee.Geometry.Polygon(bbox);
  var countyName = feature.get('ADM2_NAME');
  var province = feature.get('ADM1_NAME');
  var roiFeature = ee.Feature(roiPolygon, {'province': province, 'county': countyName});
  return roiFeature;
};
var roiPolygons = kenyaCounties.map(getRoiPolygon);

function dailyWeatherDataset(roiData, scale){
  var province = roiData.get('province');
  var county = roiData.get('county');
  var roi = roiData.geometry();
  var polygon = roi.coordinates().get(0);  
  
  var dataset = ee.ImageCollection('ECMWF/ERA5/DAILY')
                    .filterDate(startDate, endDate)
                    .filterBounds(roi);

  var weatherDataset = dataset.map(function (image) {
    var date = ee.Date(image.get('system:time_start')).format("YYYY-MM-dd");
    var minTemp = image.reduceRegion({
      reducer: ee.Reducer.min(),
      geometry: roi,
      scale: scale,
      maxPixels: 1e13
    }).get('minimum_2m_air_temperature');
    
    var maxTemp = image.reduceRegion({
      reducer: ee.Reducer.max(),
      geometry: roi,
      scale: scale,
      maxPixels: 1e13
    }).get('maximum_2m_air_temperature');  
    
    var meanTemp = image.reduceRegion({
      reducer: ee.Reducer.mean(),
      geometry: roi,
      scale: scale,
      maxPixels: 1e13
    }).get('mean_2m_air_temperature');  
    
    var totalPrecip = image.reduceRegion({
      reducer: ee.Reducer.sum(),
      geometry: roi,
      scale: scale,
      maxPixels: 1e13
    }).get('total_precipitation'); 
    
    var meanDewpoint = image.reduceRegion({
      reducer: ee.Reducer.mean(),
      geometry: roi,
      scale: scale,
      maxPixels: 1e13
    }).get('dewpoint_2m_temperature');
    
    var meanSeaLevelPressure = image.select('mean_sea_level_pressure').divide(100).set(
        'system:time_start', image.get('system:time_start')).reduceRegion({
      reducer: ee.Reducer.mean(),
      geometry: roi,
      scale: scale,
      maxPixels: 1e13
    }).get('mean_sea_level_pressure');
      
    var meanSurfacePressure = image.select('surface_pressure').divide(100).set(
        'system:time_start', image.get('system:time_start')).reduceRegion({
      reducer: ee.Reducer.mean(),
      geometry: roi,
      scale: scale,
      maxPixels: 1e13
    }).get('surface_pressure');
    
    var meanUWind10m = image.reduceRegion({
      reducer: ee.Reducer.mean(),
      geometry: roi,
      scale: scale,
      maxPixels: 1e13
    }).get('u_component_of_wind_10m');  
    
    var meanVWind10m = image.reduceRegion({
      reducer: ee.Reducer.mean(),
      geometry: roi,
      scale: scale,
      maxPixels: 1e13
    }).get('v_component_of_wind_10m')
    
    return ee.Feature(null, {
        "county": county, 
        "province": province, 
        "polygon": polygon, 
        "date": date, 
        "min_2m_temp (K)": minTemp, 
        "max_2m_temp (K)": maxTemp, 
        "mean_2m_temp (K)": meanTemp, 
        "total_precip": totalPrecip, 
        "mean_2m_dewpoint (K)": meanDewpoint, 
        "mean_sea_level_pressure (hPa)": meanSeaLevelPressure, 
        "mean_surface_pressure (hPa)": meanSurfacePressure, 
        "mean_u_wind_10m": meanUWind10m, 
        "mean_v_wind_10m": meanVWind10m
    });
});
  return weatherDataset;
}

var weatherData = roiPolygons.map(dailyWeatherDataset).flatten();

Export.table.toDrive({
  collection: weatherData,
  description: dataset_name,
  fileFormat: 'CSV',
  folder: 'google-earth',
  selectors: [
        "county", "province", "polygon", "date", "min_2m_temp (K)",  
        "max_2m_temp (K)", "mean_2m_temp (K)", "total_precip",  
        "mean_2m_dewpoint (K)", "mean_sea_level_pressure (hPa)",  
        "mean_surface_pressure (hPa)", "mean_u_wind_10m", "mean_v_wind_10m"
    
    ]
});

Map.setCenter(37.9053, 0.5358, 6);