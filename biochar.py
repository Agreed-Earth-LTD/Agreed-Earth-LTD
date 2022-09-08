#%%
import ee 
import geemap

# Initialize the map.
Map = geemap.Map()

ee.Initialize()

geometry = ee.Geometry({
    "type": "GeometryCollection",
    "geometries": [
      {
        "type": "Polygon",
        "coordinates": [
          [
            [
              -0.04993847670107243,
              53.02013274819335
            ],
            [
              -0.38227490248232243,
              52.56005253649636
            ],
            [
              0.7740361326739276,
              52.355872410218716
            ],
            [
              1.2217290037676776,
              52.628457998021
            ]
          ]
        ],
        "evenOdd": True
      },
      {
        "type": "Polygon",
        "coordinates": [
          [
            [
              0.2585811692974582,
              52.37317625811167
            ],
            [
              0.19231987779355197,
              52.32389183738869
            ],
            [
              0.23454857652402072,
              52.25816383030695
            ],
            [
              0.2949733812115207,
              52.26867005767599
            ],
            [
              0.2716274339458957,
              52.3291374727909
            ],
            [
              0.3141994554302707,
              52.3509526410338
            ]
          ]
        ],
        "evenOdd": True
      },
      {
        "type": "Polygon",
        "coordinates": [
          [
            [
              0.43653869662648503,
              52.53767043809466
            ],
            [
              0.42829895053273503,
              52.52054365167632
            ],
            [
              0.4938735965288288,
              52.507589695874884
            ],
            [
              0.5302658084428913,
              52.53975861368467
            ],
            [
              0.43722534213429753,
              52.5558342391682
            ],
            [
              0.42623901400929753,
              52.54664888847069
            ]
          ]
        ],
        "evenOdd": True
      },
      {
        "type": "Point",
        "coordinates": [
          -2.590059361205972,
          51.93216033210053
        ]
      }
    ],
    "coordinates": []
  })

geometry2 = ee.Geometry.Polygon(
      [[[-0.9891006262145252, 52.88841512036327],
        [-1.0220596105895252, 52.65245307827428],
        [-0.6375381262145252, 52.6391213713967],
        [-0.6183120519957752, 52.866866126248404]]])

dem = ee.Image("USGS/SRTMGL1_003")
sentinel = ee.ImageCollection("COPERNICUS/S2_SR")
point =ee.Geometry.Point([-0.8944781586287331, 52.87086597555083])
precipitation = ee.ImageCollection("NASA/GPM_L3/IMERG_V06")
soils = ee.Image("OpenLandMap/SOL/SOL_GRTGROUP_USDA-SOILTAX_C/v01")
visualization = {"bands":["grtgroup"],"min":0,"max":433,"palette":["FFFFFF","ADFF2D","ADFF22","A5FF2F","87FF37","BAF019",
                    "87FF19","96F03D","A3F52F","AFF319","91FF37","9CF319","9BFF37","91FF19","71FF37","86FF19","A9D42D",
                    "AFF519","9BFF19","9AF024","A5FD2F","88FF37","AFED19","71FF19","AFF026","8CF537","B7FF19","7177C0","9A85EC",
                    "F5F5E1","52CF5A","E42777","4EF76D","FF00FB","EB05EB","FA04FA","FC04F5","F50DF0","F118F1","FA0CFA","FC05E1",
                    "F100D5","EB09E6","FA22FA","FFDAB9","F5D2BB","E8C9B8","FFDDC4","E7CBC0","FFD2C3","F5D6BB","D5D3B9","E8D4B8",
                    "E7CDC0","F3EAC8","A0C4BA","FFD2B9","F5DABB","F5D5B9","E8EBB8","FFDDC2","E7FFC0","F3E6C8","FFDAB9","F5CDB9",
                    "A91D30","796578","D8FF6E","177548","43EFD6","8496A9","296819","73FFD4","6FFFC8","75FBC9","86F5D1","82FFD2",
                    "88EEC8","80FFD4","6BFFC9","88EEC8","7FFFC8","81FFD2","86F0D4","67FFC8","88EEC8","7FFBCB","87FFD2","8AF5CE",
                    "6BFAD2","78F0D4","88EEC8","7FFBD4","73F5CD","88C8D2","91F0CD","73CDD2","88EEC8","FB849B","DD4479","61388B",
                    "A52A30","722328","D81419","A42828","82F5CD","A54C2E","C11919","B91419","21B199","702028","B41919","B22328",
                    "A2C7EB","36BA79","806797","CB5B5F","CD5C5C","D94335","D35740","E05A5D","CF5B5C","CA5964","CA5D5F","CD5E5A",
                    "CA5969","D95A35","D36240","E05C43","D64755","CF595C","FF5F5F","CD6058","D95F35","D35140","D65A55","E05C59",
                    "CF525E","C65978","F5615F","826F9A","CFF41A","4A6F31","A96989","E16438","24F640","88C1F9","F5D25C","D74322",
                    "7F939E","41A545","8F8340","09FE03","0AFF00","0FF30F","02F00A","0FC903","17F000","0CFF00","0AC814","0CFE00",
                    "0AFF0A","03FF05","1CF31C","24F000","00FF0C","14C814","00FE4C","14FF96","44D205","05F305","62F00A","0FCD03",
                    "00D20F","1ADD11","09FF0C","03FF05","05E700","02F00A","0FEA03","00F000","0CCB0C","14DD14","6A685D","FAE6B9",
                    "769A34","6FF2DF","CA7FC6","D8228F","C01BF0","D2BAD3","D8C3CB","D4C6D4","D5BED5","DDB9DD","D8D2D8","D4C9D4",
                    "D2BAD5","D5BAD5","D5B2D5","D8C8D2","D4CBD4","552638","2571EB","FFA514","F3A502","FB7B00","F0B405","F7A80F",
                    "FB9113","FFA519","F3A702","FBBA07","F7970F","F3A702","FB5A00","F0C005","F7810F","FF9C00","F3B002","F0B005",
                    "F7980F","4D7CFC","FFFF00","FAFA05","EBEB22","FFFF14","F1F10A","FAFA05","EBEB1E","F5EB0C","EEF506","F1F129",
                    "FAFA05","EBEB0C","F5D202","FFD700","F1F12B","A91FAC","2DA468","9A8B71","76B989","713959"]}
sample_export = ee.Geometry.Polygon(
      [[[0.14023444040608624, 52.2995545949096],
        [0.14023444040608624, 52.261011411148814],
        [0.20718237741780499, 52.261011411148814],
        [0.20718237741780499, 52.2995545949096]]], None, False)


#Cloud masking for Sentinel-2 lvl2A imagery
def cloudmask(image):
    mask = image.select('SCL').gte(8).And(image.select('SCL').neq(11))
    return image.mask(mask.neq(1))

sentinel = sentinel.map(cloudmask)
#Map.addLayer(cloudmask,{min:0,max:8000,gamma:1.4,bands:['B4','B3','B2']})

#Load UK boundaries from FAO dataset
table = ee.FeatureCollection("FAO/GAUL/2015/level0")

table = table.filterMetadata('ADM0_CODE','equals',256)

#Load COPERNICUS LANCOVER dataset
copernicus = ee.ImageCollection("COPERNICUS/Landcover/100m/Proba-V-C3/Global")
copernicus = copernicus.select('crops-coverfraction').mosaic().clip(table)
Map.addLayer(copernicus,{'min':0, 'max':100, 'palette':['red','yellow','green']},'crops-coverfraction',0)

#Load 2018 CORINE land cover dataset
dataset = ee.Image('COPERNICUS/CORINE/V20/100m/2018')
landCover = dataset.select('landcover')
landCover = landCover.clip(table)
Map.addLayer(landCover, {}, 'Land Cover',0)

#Mask Agricultural areas > Arable land > Non-irrigated arable land (211)
mask = landCover.eq(211)
mask = mask.mask(mask)
Map.addLayer(mask,{'palette':'red'},'Non-irrigated arable land',0)


#Mask Agricultural areas > Arable land > Permanently irrigated land
mask2 = landCover.eq(212)
mask2 = mask2.mask(mask2)
Map.addLayer(mask2,{'palette':'cyan'},'Permanently irrigated land',0)

#Center the map canvas into the UK boundaries with a 5 zoom level
Map.centerObject(table,5)

#Get slope data in degrees
slope = ee.Terrain.slope(dem)
slope = slope.clip(table)
Map.addLayer(slope,{'min':0, 'max':10},'Slope (degrees)',0)

#Mask slope above 10�
slope_mask10 = slope.gt(10)
slope_mask10 = slope_mask10.mask(slope_mask10)
Map.addLayer(slope_mask10,{'palette':'green'},'Slope higher than 10�',0)

#%%
#Obtain Non-irrigated arable land surface for UK
areaImage = mask.multiply(ee.Image.pixelArea())
area_211 = ee.Number(areaImage.reduceRegion(**{
    'reducer': ee.Reducer.sum(),
    'geometry': table,
    'scale': 100,
    'maxPixels': 1e10
    }).get('landcover')).divide(1e4).round()
# print('Non-irrigated arable land surface (ha)',area_211)

#Obtain Permanently irrigated land
areaImage_p = mask2.multiply(ee.Image.pixelArea())
area_212 = ee.Number(areaImage_p.reduceRegion(**{
    'reducer': ee.Reducer.sum(),
    'geometry': table,
    'scale': 100,
    'maxPixels': 1e10
    }).get('landcover')).divide(1e4).round()
# print('Permanently irrigated land surface (ha)',area_212)

#Obtain +10� slope surface for UK
areaImage2 = slope_mask10.multiply(ee.Image.pixelArea())
areaslope = ee.Number(areaImage2.reduceRegion(**{
    'reducer': ee.Reducer.sum(),
    'geometry': table,
    'scale':30,
    'maxPixels': 1e10
    }).get('slope')).divide(1e4).round()
# print('+10� slope surface (ha)',areaslope)

#Obtain mask for Non-irrigated arable lands and slope +10�
mask_land_slope = mask.eq(1).And(slope_mask10.eq(1))
mask_land_slope = mask_land_slope.mask(mask_land_slope)
Map.addLayer(mask_land_slope,{'palette':['orange']},'Mask arable land and slope >10�',0)

#Calculate area for above mask
areaImage3 = mask_land_slope.multiply(ee.Image.pixelArea())
totalarea = ee.Number(areaImage3.reduceRegion(**{
    'reducer': ee.Reducer.sum(),
    'geometry': table,
    'scale': 30,
    'maxPixels': 1e10
    }).get('landcover')).divide(1e4).round()
# print('Non-irrigated arable land surface and +10� slope surface (ha)',totalarea)

#Mask crop cover fraction
crop_mask = copernicus.gte(80)
crop_mask = crop_mask.mask(crop_mask)
Map.addLayer(crop_mask,{'palette':'blue'},'Crop cover fraction >80%',0)

#Mask slope greater than 5�
slope_mask5 = slope.gte(5)
slope_mask5 = slope_mask5.mask(slope_mask5)
Map.addLayer(slope_mask5,{'palette':'purple'},'Slope higher than 5�',0)

#Mask crop cover +80% and slope +5�
cc_slope = crop_mask.eq(1).And(slope_mask5.eq(1))
cc_slope = cc_slope.mask(cc_slope)
Map.addLayer(cc_slope,{'palette':'red'},'Mask crop cover >80% and slope >5�',0)

#Calculate area for above mask
areaImage4 = cc_slope.multiply(ee.Image.pixelArea())
totalarea4 = ee.Number(areaImage4.reduceRegion(**{
    'reducer': ee.Reducer.sum(),
    'geometry': table,
    'scale': 30,
    'maxPixels': 1e10
    }).get('crops-coverfraction')).divide(1e4).round()
# print('Crop cover +80% and slope higher than 5� (ha)',totalarea4)

#Load cloud-masked pixels for Sentinel-2 dataset, June 2020
def func_gkp(image):
    return image.clip(table)

sen = sentinel \
    .map(cloudmask) \
    .filterBounds(table) \
    .filterDate('2020-6-1','2020-7-1') \
    .map(func_gkp)

sen = sen.reduce(ee.Reducer.median())
Map.addLayer(sen,{'min':0, 'max':8000, 'gamma':1.4, 'bands':['B4_median','B3_median','B2_median']},'Sentinel-2 June 2020')

#NDVI Calculation
ndvi = sen.normalizedDifference(['B8_median','B4_median'])
Map.addLayer(ndvi,{'min':-1, 'max':1, 'palette':['red','yellow','green']},'NDVI',0)

#NDVI masking (values greater than 0.8)
ndvi_mask = ndvi.gt(0.8)
ndvi_mask = ndvi_mask.selfMask()
Map.addLayer(ndvi_mask,{'palette':'black'},'NDVI Mask +0.8',0)


#BSI EXPRESSION

def func_joo(image):
    return image.select().addBands(image.expression(
    '((B11+B4)-(B8+B2))/((B11+B4)+(B8+B2))',
    {
        'B11': image.select('B11'),
        'B4': image.select('B4'),
        'B8': image.select('B8'),
        'B2': image.select('B2')
    })).rename('BSI')

bsi = sentinel.map(func_joo)

bsi2 = bsi \
    .filterDate('2020-1-1','2020-12-31') \
    .filterBounds(table)
#.filter(ee.Filter.metadata('CLOUDY_PIXEL_PERCENTAGE','less_than',10))
#print(bsi2)
#Map.addLayer(bsi,{min:-1,max:1,palette:['red','yellow','green']},'Bare Soil Index',0)

#Filter BSI dataset
bsi_june = bsi.filterBounds(table) \
    .filterDate('2020-6-1','2020-7-1') \
    .filterMetadata('CLOUDY_PIXEL_PERCENTAGE','less_than',9) \
    .mosaic() \
    .clip(table)
Map.addLayer(bsi_june,{'min':-1, 'max':1, 'palette':['red','yellow','green']},'Bare Soil Index June 2020',0)

#BSI average value per month 2020
months = ee.List.sequence(1, 12)
years = ee.List.sequence(2020,2020)

#%%

def mo (y,m):
  return bsi2 \
    .filter(ee.Filter.calendarRange(y, y, 'year')) \
    .filter(ee.Filter.calendarRange(m, m, 'month')) \
    .mean() \
    .set('month', m).set('year', y)

byMonthYear = ee.ImageCollection.fromImages( \
  years.map(lambda y : months.map(lambda m : mo(y,m))).flatten())

byMonthYear = byMonthYear.map(lambda image: ee.Image(image).clip(table))
print('Mean BSI 2020')#,byMonthYear)

#Map.addLayer(byMonthYear,{min:-0.3,max:0.2,palette:['red','orange','yellow','green']},'Mean BSI per month -year 2020-')
Map.addLayer(byMonthYear.filterMetadata('month','equals',2),{'min':-0.3, 'max':0.2, 'palette':['red','orange','yellow','green']},'Mean BSI Feb 2020')
Map.addLayer(byMonthYear.filterMetadata('month','equals',3),{'min':-0.3, 'max':0.2, 'palette':['red','orange','yellow','green']},'Mean BSI Mar 2020')
Map.addLayer(byMonthYear.filterMetadata('month','equals',1),{'min':-0.3, 'max':0.2, 'palette':['red','orange','yellow','green']},'Mean BSI Jan 2020')
Map.addLayer(byMonthYear.filterMetadata('month','equals',4),{'min':-0.3, 'max':0.2, 'palette':['red','orange','yellow','green']},'Mean BSI Apr 2020')
Map.addLayer(byMonthYear.filterMetadata('month','equals',5),{'min':-0.3, 'max':0.2, 'palette':['red','orange','yellow','green']},'Mean BSI May 2020')
Map.addLayer(byMonthYear.filterMetadata('month','equals',6),{'min':-0.3, 'max':0.2, 'palette':['red','orange','yellow','green']},'Mean BSI Jun 2020')
Map.addLayer(byMonthYear.filterMetadata('month','equals',7),{'min':-0.3, 'max':0.2, 'palette':['red','orange','yellow','green']},'Mean BSI Jul 2020')
Map.addLayer(byMonthYear.filterMetadata('month','equals',8),{'min':-0.3, 'max':0.2, 'palette':['red','orange','yellow','green']},'Mean BSI Aug 2020')
Map.addLayer(byMonthYear.filterMetadata('month','equals',9),{'min':-0.3, 'max':0.2, 'palette':['red','orange','yellow','green']},'Mean BSI Sep 2020')
Map.addLayer(byMonthYear.filterMetadata('month','equals',10),{'min':-0.3, 'max':0.2, 'palette':['red','orange','yellow','green']},'Mean BSI Oct 2020')
Map.addLayer(byMonthYear.filterMetadata('month','equals',11),{'min':-0.3, 'max':0.2, 'palette':['red','orange','yellow','green']},'Mean BSI Nov 2020')
Map.addLayer(byMonthYear.filterMetadata('month','equals',12),{'min':-0.3, 'max':0.2, 'palette':['red','orange','yellow','green']},'Mean BSI Dec 2020')


#------------------------------------------MEAN NDVI PER MONTH 2020-----------------------------------
#ADD MSAVI "BAND" TO SENTINEL DATASET

def func_pdp(image):
  return image.select().addBands(image.expression( \
    '(2*NIR + 1 - sqrt((2*NIR + 1)*(2*NIR + 1) - 8*(NIR - RED)))/2', \
    {'NIR': image.select('B8'),'RED': image.select('B4')})).rename('MSAVI')

msavi = sentinel.map(func_pdp)

msavi2 = msavi \
.filterDate('2020-1-1','2020-12-31') \
.filterBounds(table)
#.filter(ee.Filter.metadata('CLOUDY_PIXEL_PERCENTAGE','less_than',10))
#print(bsi2)
#Map.addLayer(bsi,{min:-1,max:1,palette:['red','yellow','green']},'Bare Soil Index',0)

#%%


def mo (y,m):
  return msavi2 \
    .filter(ee.Filter.calendarRange(y, y, 'year')) \
    .filter(ee.Filter.calendarRange(m, m, 'month')) \
    .mean() \
    .set('month', m).set('year', y)

byMonthYear_msavi = ee.ImageCollection.fromImages( \
  years.map(lambda y : months.map(lambda m : mo(y,m))).flatten())

byMonthYear_msavi = byMonthYear_msavi.map(lambda image: ee.Image(image).clip(table))
print('Mean MSAVI 2020')#,byMonthYear_msavi)


#Map.addLayer(byMonthYear,{min:-0.3,max:0.2,palette:['red','orange','yellow','green']},'Mean BSI per month -year 2020-')
Map.addLayer(byMonthYear_msavi.filterMetadata('month','equals',1),{'min':-1, 'max':1, 'palette':['#a6611a','#dfc27d','#f5f5f5','#80cdc1','#018571']},'Mean MSAVI Jan 2020')
Map.addLayer(byMonthYear_msavi.filterMetadata('month','equals',2),{'min':-1, 'max':1, 'palette':['#a6611a','#dfc27d','#f5f5f5','#80cdc1','#018571']},'Mean MSAVI Feb 2020')
Map.addLayer(byMonthYear_msavi.filterMetadata('month','equals',3),{'min':-1, 'max':1, 'palette':['#a6611a','#dfc27d','#f5f5f5','#80cdc1','#018571']},'Mean MSAVI Mar 2020')
Map.addLayer(byMonthYear_msavi.filterMetadata('month','equals',4),{'min':-1, 'max':1, 'palette':['#a6611a','#dfc27d','#f5f5f5','#80cdc1','#018571']},'Mean MSAVI Apr 2020')
Map.addLayer(byMonthYear_msavi.filterMetadata('month','equals',5),{'min':-1, 'max':1, 'palette':['#a6611a','#dfc27d','#f5f5f5','#80cdc1','#018571']},'Mean MSAVI May 2020')
Map.addLayer(byMonthYear_msavi.filterMetadata('month','equals',6),{'min':-1, 'max':1, 'palette':['#a6611a','#dfc27d','#f5f5f5','#80cdc1','#018571']},'Mean MSAVI Jun 2020')
Map.addLayer(byMonthYear_msavi.filterMetadata('month','equals',7),{'min':-1, 'max':1, 'palette':['#a6611a','#dfc27d','#f5f5f5','#80cdc1','#018571']},'Mean MSAVI Jul 2020')
Map.addLayer(byMonthYear_msavi.filterMetadata('month','equals',8),{'min':-1, 'max':1, 'palette':['#a6611a','#dfc27d','#f5f5f5','#80cdc1','#018571']},'Mean MSAVI Aug 2020')
Map.addLayer(byMonthYear_msavi.filterMetadata('month','equals',9),{'min':-1, 'max':1, 'palette':['#a6611a','#dfc27d','#f5f5f5','#80cdc1','#018571']},'Mean MSAVI Sep 2020')
Map.addLayer(byMonthYear_msavi.filterMetadata('month','equals',10),{'min':-1, 'max':1, 'palette':['#a6611a','#dfc27d','#f5f5f5','#80cdc1','#018571']},'Mean MSAVI Oct 2020')
Map.addLayer(byMonthYear_msavi.filterMetadata('month','equals',11),{'min':-1, 'max':1, 'palette':['#a6611a','#dfc27d','#f5f5f5','#80cdc1','#018571']},'Mean MSAVI Nov 2020')
Map.addLayer(byMonthYear_msavi.filterMetadata('month','equals',12),{'min':-1, 'max':1, 'palette':['#a6611a','#dfc27d','#f5f5f5','#80cdc1','#018571']},'Mean MSAVI Dec 2020')

#------------------------------------------------MEAN MSAVI PER MONTH 2020---------------------------
#ADD NDVI "BAND" TO SENTINEL DATASET

def func_yvb(image):
  return image.select().addBands(image.normalizedDifference(['B8','B4'])).rename('NDVI')

ndvi_cloudy = sentinel.map(func_yvb)

#%%


ndvi_cloudy2 = ndvi_cloudy \
  .filterDate('2020-1-1','2020-12-31') \
  .filterBounds(table)
#.filter(ee.Filter.metadata('CLOUDY_PIXEL_PERCENTAGE','less_than',10))
#print(bsi2)
#Map.addLayer(bsi,{min:-1,max:1,palette:['red','yellow','green']},'Bare Soil Index',0)


def mo (y,m):
  return ndvi_cloudy2 \
    .filter(ee.Filter.calendarRange(y, y, 'year')) \
    .filter(ee.Filter.calendarRange(m, m, 'month')) \
    .mean() \
    .set('month', m).set('year', y)

byMonthYear_ndvi = ee.ImageCollection.fromImages( \
  years.map(lambda y : months.map(lambda m : mo(y,m))).flatten())

byMonthYear_ndvi = byMonthYear_ndvi.map(lambda image: ee.Image(image).clip(table))
print('Mean NDVI 2020')#,byMonthYear_ndvi)


#Map.addLayer(byMonthYear,{min:-0.3,max:0.2,palette:['red','orange','yellow','green']},'Mean BSI per month -year 2020-')
Map.addLayer(byMonthYear_ndvi.filterMetadata('month','equals',1),{'min':-1, 'max':1, 'palette':['#f7fcf5','#caeac3','#7bc87c','#2a924a','#00441b']},'Mean NDVI Jan 2020')
Map.addLayer(byMonthYear_ndvi.filterMetadata('month','equals',2),{'min':-1, 'max':1, 'palette':['#f7fcf5','#caeac3','#7bc87c','#2a924a','#00441b']},'Mean NDVI Feb 2020')
Map.addLayer(byMonthYear_ndvi.filterMetadata('month','equals',3),{'min':-1, 'max':1, 'palette':['#f7fcf5','#caeac3','#7bc87c','#2a924a','#00441b']},'Mean NDVI Mar 2020')
Map.addLayer(byMonthYear_ndvi.filterMetadata('month','equals',4),{'min':-1, 'max':1, 'palette':['#f7fcf5','#caeac3','#7bc87c','#2a924a','#00441b']},'Mean NDVI Apr 2020')
Map.addLayer(byMonthYear_ndvi.filterMetadata('month','equals',5),{'min':-1, 'max':1, 'palette':['#f7fcf5','#caeac3','#7bc87c','#2a924a','#00441b']},'Mean NDVI May 2020')
Map.addLayer(byMonthYear_ndvi.filterMetadata('month','equals',6),{'min':-1, 'max':1, 'palette':['#f7fcf5','#caeac3','#7bc87c','#2a924a','#00441b']},'Mean NDVI Jun 2020')
Map.addLayer(byMonthYear_ndvi.filterMetadata('month','equals',7),{'min':-1, 'max':1, 'palette':['#f7fcf5','#caeac3','#7bc87c','#2a924a','#00441b']},'Mean NDVI Jul 2020')
Map.addLayer(byMonthYear_ndvi.filterMetadata('month','equals',8),{'min':-1, 'max':1, 'palette':['#f7fcf5','#caeac3','#7bc87c','#2a924a','#00441b']},'Mean NDVI Aug 2020')
Map.addLayer(byMonthYear_ndvi.filterMetadata('month','equals',9),{'min':-1, 'max':1, 'palette':['#f7fcf5','#caeac3','#7bc87c','#2a924a','#00441b']},'Mean NDVI Sep 2020')
Map.addLayer(byMonthYear_ndvi.filterMetadata('month','equals',10),{'min':-1, 'max':1, 'palette':['#f7fcf5','#caeac3','#7bc87c','#2a924a','#00441b']},'Mean NDVI Oct 2020')
Map.addLayer(byMonthYear_ndvi.filterMetadata('month','equals',11),{'min':-1, 'max':1, 'palette':['#f7fcf5','#caeac3','#7bc87c','#2a924a','#00441b']},'Mean NDVI Nov 2020')
Map.addLayer(byMonthYear_ndvi.filterMetadata('month','equals',12),{'min':-1, 'max':1, 'palette':['#f7fcf5','#caeac3','#7bc87c','#2a924a','#00441b']},'Mean NDVI Dec 2020')

#-----------------------------------------------------------------------------------------------------
#BSI masking (values greater than 0.1)
bsi_mask = bsi_june.gt(0.1)
bsi_mask = bsi_mask.mask(bsi_mask)
Map.addLayer(bsi_mask,{'palette':'black'},'BSI Mask +0.1',0)

#BSI masking (values greater than 0.05)
bsi_mask2 = bsi_june.gt(0.05)
bsi_mask2 = bsi_mask2.mask(bsi_mask2)
Map.addLayer(bsi_mask2,{'palette':'olive'},'BSI Mask +0.05',0)

#Soil Moisture Index calculation (0.9)
msi = sen.normalizedDifference(['B8_median','B11_median'])
Map.addLayer(ndvi,{'min':-1, 'max':1, 'palette':['red','yellow','green']},'NDMI',0)

#NDMI Masking (0.5)
msi_mask = msi.gt(0.5)
msi_mask = msi_mask.mask(msi_mask)
Map.addLayer(msi_mask,{'palette':'yellow'},'NDMI Mask +0.5',0)

#BSI +0.1 and Slope +5� mask
bsi_slope = bsi_june.gt(0.1).And(slope.gt(5))
bsi_slope = bsi_slope.mask(bsi_slope)
Map.addLayer(bsi_slope,{'palette':'orange'},'BSI +0.1 and Slope +5�')
#
#%%
#Clip precipitation
# precipitation = precipitation

# def func_ipa(image)return image.clip(table)};: \
# .map(function(image){return image.clip(table)} \
# .map(func_ipa)


# #January
# precipitation_jan = precipitation.select('IRprecipitation') \
# .filterDate('2021-1-1','2021-2-1')

# pp_acum_jan = precipitation_jan \
# .reduce(ee.Reducer.sum())
# print(pp_acum_jan)
# Map.addLayer(pp_acum_jan,{'min':0, 'max':200, 'palette':['#1E90FF','#187DE9','#126AD2','#0C56BC','#0643A5','#00308F']},'Accumulated precipitation January 2021',0)

# #February
# precipitation_feb = precipitation.select('IRprecipitation') \
# .filterDate('2021-2-1','2021-3-1')

# pp_acum_feb = precipitation_feb \
# .reduce(ee.Reducer.sum())
# print(pp_acum_feb)
# Map.addLayer(pp_acum_feb,{'min':0, 'max':200, 'palette':['#1E90FF','#187DE9','#126AD2','#0C56BC','#0643A5','#00308F']},'Accumulated precipitation February 2021',0)

# #March
# precipitation_march = precipitation.select('IRprecipitation') \
# .filterDate('2021-3-1','2021-4-1')

# pp_acum_march = precipitation_march \
# .reduce(ee.Reducer.sum())
# print(pp_acum_march)
# Map.addLayer(pp_acum_march,{'min':0, 'max':200, 'palette':['#1E90FF','#187DE9','#126AD2','#0C56BC','#0643A5','#00308F']},'Accumulated precipitation March 2021',0)

# #April
# precipitation_apr = precipitation.select('IRprecipitation') \
# .filterDate('2021-4-1','2021-5-1')

# pp_acum_apr = precipitation_apr \
# .reduce(ee.Reducer.sum())
# print(pp_acum_apr)
# Map.addLayer(pp_acum_apr,{'min':0, 'max':200, 'palette':['#1E90FF','#187DE9','#126AD2','#0C56BC','#0643A5','#00308F']},'Accumulated precipitation April 2021',0)

# #May
# precipitation_may = precipitation.select('IRprecipitation') \
# .filterDate('2021-5-1','2021-6-1')

# pp_acum_may = precipitation_may \
# .reduce(ee.Reducer.sum())
# print(pp_acum_may)
# Map.addLayer(pp_acum_may,{'min':0, 'max':200, 'palette':['#1E90FF','#187DE9','#126AD2','#0C56BC','#0643A5','#00308F']},'Accumulated precipitation May 2021',0)

# #June
# precipitation_jun = precipitation.select('IRprecipitation') \
# .filterDate('2021-6-1','2021-7-1')

# pp_acum_jun = precipitation_jun \
# .reduce(ee.Reducer.sum())
# print(pp_acum_jun)
# Map.addLayer(pp_acum_jun,{'min':0, 'max':200, 'palette':['#1E90FF','#187DE9','#126AD2','#0C56BC','#0643A5','#00308F']},'Accumulated precipitation June 2021',0)


# #July
# precipitation_jul = precipitation.select('IRprecipitation') \
# .filterDate('2021-7-1','2021-8-1')

# pp_acum_jul = precipitation_jul \
# .reduce(ee.Reducer.sum())
# print(pp_acum_jul)
# Map.addLayer(pp_acum_jul,{'min':0, 'max':200, 'palette':['#1E90FF','#187DE9','#126AD2','#0C56BC','#0643A5','#00308F']},'Accumulated precipitation July 2021',0)

# #August
# precipitation_aug = precipitation.select('IRprecipitation') \
# .filterDate('2021-8-1','2021-9-1')

# pp_acum_aug = precipitation_aug \
# .reduce(ee.Reducer.sum())
# print(pp_acum_aug)
# Map.addLayer(pp_acum_aug,{'min':0, 'max':200, 'palette':['#1E90FF','#187DE9','#126AD2','#0C56BC','#0643A5','#00308F']},'Accumulated precipitation August 2021',0)

# #September
# precipitation_sep = precipitation.select('IRprecipitation') \
# .filterDate('2021-9-1','2021-10-1')

# pp_acum_sep = precipitation_sep \
# .reduce(ee.Reducer.sum())
# print(pp_acum_sep)
# Map.addLayer(pp_acum_sep,{'min':0, 'max':200, 'palette':['#1E90FF','#187DE9','#126AD2','#0C56BC','#0643A5','#00308F']},'Accumulated precipitation September 2021',0)

# #October
# precipitation_oct = precipitation.select('IRprecipitation') \
# .filterDate('2021-10-1','2021-11-1')

# pp_acum_oct = precipitation_oct \
# .reduce(ee.Reducer.sum())
# print(pp_acum_oct)
# Map.addLayer(pp_acum_oct,{'min':0, 'max':200, 'palette':['#1E90FF','#187DE9','#126AD2','#0C56BC','#0643A5','#00308F']},'Accumulated precipitation October 2021',0)
# #

#Load soils
soils = soils.clip(table)
# print(soils)

Map.addLayer(soils, visualization, "USDA soil taxonomy great groups")

#Soil moisture dataset
ssm = ee.ImageCollection("NASA_USDA/HSL/SMAP10KM_soil_moisture") \
  .select('ssm') \
  .filterDate('2020-1-1','2020-12-31') \
  .map(lambda x: x.clip(table)) 

Map.addLayer(ssm,{'min':0, 'max':28, 'palette': ['0300ff', '418504', 'efff07', 'efff07', 'ff0303']},'Soil Moisture Data')
print('Soil moisture dataset')#,ssm)

#Mean SSM JAN 2020
#ssm1 = ssm.filterDate('2020-1-1','2020-1-31')
#ssm1 = ssm1.reduce(ee.Reducer.mean())
Map.addLayer(ssm.filterDate('2020-1-1','2020-1-31').reduce(ee.Reducer.mean()),{'min':0, 'max':28, 'palette': ['0300ff', '418504', 'efff07', 'efff07', 'ff0303']},'Soil Moisture Data Jan 2020')

#Mean SSM FEB 2020
#ssm2 = ssm.filterDate('2020-2-1','2020-2-29')
#ssm2 = ssm2.reduce(ee.Reducer.mean())
Map.addLayer(ssm.filterDate('2020-2-1','2020-2-29').reduce(ee.Reducer.mean()),{'min':0, 'max':28, 'palette': ['0300ff', '418504', 'efff07', 'efff07', 'ff0303']},'Soil Moisture Data Feb 2020')

#Mean SSM MAR 2020
#ssm3 = ssm.filterDate('2020-3-1','2020-3-31')
#ssm3 = ssm3.reduce(ee.Reducer.mean())
Map.addLayer(ssm.filterDate('2020-3-1','2020-3-31').reduce(ee.Reducer.mean()),{'min':0, 'max':28, 'palette': ['0300ff', '418504', 'efff07', 'efff07', 'ff0303']},'Soil Moisture Data Mar 2020')

#Mean SSM APR 2020
#ssm4 = ssm.filterDate('2020-4-1','2020-4-30')
#ssm4 = ssm4.reduce(ee.Reducer.mean())
Map.addLayer(ssm.filterDate('2020-4-1','2020-4-30').reduce(ee.Reducer.mean()),{'min':0, 'max':28, 'palette': ['0300ff', '418504', 'efff07', 'efff07', 'ff0303']},'Soil Moisture Data Apr 2020')

#Mean SSM MAY 2020
#ssm5 = ssm.filterDate('2020-5-1','2020-5-31')
#ssm5 = ssm5.reduce(ee.Reducer.mean())
Map.addLayer(ssm.filterDate('2020-5-1','2020-5-31').reduce(ee.Reducer.mean()),{'min':0, 'max':28, 'palette': ['0300ff', '418504', 'efff07', 'efff07', 'ff0303']},'Soil Moisture Data May 2020')

#Mean SSM JUN 2020
#ssm6 = ssm.filterDate('2020-6-1','2020-6-30')
#ssm6 = ssm6.reduce(ee.Reducer.mean())
Map.addLayer(ssm.filterDate('2020-6-1','2020-6-30').reduce(ee.Reducer.mean()),{'min':0, 'max':28, 'palette': ['0300ff', '418504', 'efff07', 'efff07', 'ff0303']},'Soil Moisture Data Jun 2020')

#Mean SSM JUL 2020
#ssm7 = ssm.filterDate('2020-7-1','2020-7-31')
#ssm7 = ssm7.reduce(ee.Reducer.mean())
Map.addLayer(ssm.filterDate('2020-7-1','2020-7-31').reduce(ee.Reducer.mean()),{'min':0, 'max':28, 'palette': ['0300ff', '418504', 'efff07', 'efff07', 'ff0303']},'Soil Moisture Data Jul 2020')

#Mean SSM AUG 2020
#ssm8 = ssm.filterDate('2020-8-1','2020-8-31')
#ssm8 = ssm8.reduce(ee.Reducer.mean())
Map.addLayer(ssm.filterDate('2020-8-1','2020-8-31').reduce(ee.Reducer.mean()),{'min':0, 'max':28, 'palette': ['0300ff', '418504', 'efff07', 'efff07', 'ff0303']},'Soil Moisture Data Aug 2020')

#Mean SSM SEP 2020
#ssm9 = ssm.filterDate('2020-9-1','2020-9-30')
#ssm9 = ssm9.reduce(ee.Reducer.mean())
Map.addLayer(ssm.filterDate('2020-9-1','2020-9-30').reduce(ee.Reducer.mean()),{'min':0, 'max':28, 'palette': ['0300ff', '418504', 'efff07', 'efff07', 'ff0303']},'Soil Moisture Data Sep 2020')

#Mean SSM OCT 2020
#ssm10 = ssm.filterDate('2020-10-1','2020-10-31')
#ssm10 = ssm10.reduce(ee.Reducer.mean())
Map.addLayer(ssm.filterDate('2020-10-1','2020-10-31').reduce(ee.Reducer.mean()),{'min':0, 'max':28, 'palette': ['0300ff', '418504', 'efff07', 'efff07', 'ff0303']},'Soil Moisture Data Oct 2020')

#Mean SSM NOV 2020
#ssm11 = ssm.filterDate('2020-11-1','2020-11-30')
#ssm11 = ssm11.reduce(ee.Reducer.mean())
Map.addLayer(ssm.filterDate('2020-11-1','2020-11-30').reduce(ee.Reducer.mean()),{'min':0, 'max':28, 'palette': ['0300ff', '418504', 'efff07', 'efff07', 'ff0303']},'Soil Moisture Data Nov 2020')

#Mean SSM DEC 2020
#ssm12 = ssm.filterDate('2020-12-1','2020-12-31')
#ssm12 = ssm12.reduce(ee.Reducer.mean())
Map.addLayer(ssm.filterDate('2020-12-1','2020-12-31').reduce(ee.Reducer.mean()),{'min':0, 'max':28, 'palette': ['0300ff', '418504', 'efff07', 'efff07', 'ff0303']},'Soil Moisture Data Dec 2020')

#
#Average value for SSM 2020 May
ssm_avg = ssm.reduce(ee.Reducer.mean())
Map.addLayer(ssm_avg,{'min':0, 'max':28, 'palette': ['0300ff', '418504', 'efff07', 'efff07', 'ff0303']},'Soil Moisture Data average')
print('Soil moisture dataset mean')#,ssm_avg)#
#Soil Texture Class
soil_texture = ee.Image("OpenLandMap/SOL/SOL_TEXTURE-CLASS_USDA-TT_M/v02") \
  .clip(table)

visualization_soil_texture = {
  'min': 1.0,
  'max': 12.0,
  'palette': [
    "d5c36b","b96947","9d3706","ae868f","f86714","46d143",
    "368f20","3e5a14","ffd557","fff72e","ff5a9d","ff005b",
  ]}
  
Map.addLayer(soil_texture.select('b0'), visualization_soil_texture, "Soil texture class (USDA system) at 0cm")
Map.addLayer(soil_texture.select('b10'), visualization_soil_texture, "Soil texture class (USDA system) at 10cm",0)
Map.addLayer(soil_texture.select('b30'), visualization_soil_texture, "Soil texture class (USDA system) at 30cm",0)
Map.addLayer(soil_texture.select('b60'), visualization_soil_texture, "Soil texture class (USDA system) at 60cm",0)
Map.addLayer(soil_texture.select('b100'), visualization_soil_texture, "Soil texture class (USDA system) at 100cm",0)
Map.addLayer(soil_texture.select('b200'), visualization_soil_texture, "Soil texture class (USDA system) at 200cm",0)

#Add Soil texture legend
# Create the panel for the legend items.
# legend = ui.Panel({
# 'style': {
#   'position': 'bottom-left',
#   'padding': '8px 15px'
# }
# })

# # Create and add the legend title.
# legendTitle = ui.Label({
# 'value': 'Soil Texture Class',
# 'style': {
#   'fontWeight': 'bold',
#   'fontSize': '18px',
#   'margin': '0 0 4px 0',
#   'padding': '0'
# }
# })
# legend.add(legendTitle)

# loading = ui.Label('Loading legend...', {'margin': '2px 0 4px 0'})
# legend.add(loading)

# # Creates and styles 1 row of the legend.
# def makeRow(color, name):
# # Create the label that is actually the colored box.
# colorBox = ui.Label({
#   'style': {
#     'backgroundColor': '#' + color,
#     # Use padding to give the box height and width.
#     'padding': '8px',
#     'margin': '0 0 4px 0'
#   }
# })

# # Create the label filled with the description text.
# description = ui.Label({
#   'value': name,
#   'style': '{margin': '0 0 4px 6px'}
# })

# return ui.Panel({
#   'widgets': [colorBox, description],
#   'layout': ui.Panel.Layout.Flow('horizontal')
# })



# # Get the list of palette colors and class names from the image.
# soil_texture.toDictionary().select(['b0' + ".*"]).evaluate(function(result) {
# palette = result['b0' + "_class_palette"]
# names = result['b0' + "_class_names"]
# loading.style().set('shown', False)

# for i in range(0, names.length, 1):
#   legend.add(makeRow(palette[i], names[i]))

# })

# Map.add(legend)
#Soil pH
ph = ee.Image("OpenLandMap/SOL/SOL_PH-H2O_USDA-4C1A2A_M/v02") \
  .clip(table) \
  .divide(10)

visualization_ph = {'bands':["b0"],
  'min':4.2,
  'max':11,
  'palette':["FF0000","FF1C00","FF3900","FF5500",
  "FF7100","FF8E00","FFAA00","FFC600","FFE200",
  "FFFF00","E3FF00","C7FF00","AAFF00","8EFF00",
  "72FF00","55FF00","39FF00","1DFF00","01FF00",
  "00FF1C","00FF38","00FF54","00FF71","00FF8D",
  "00FFA9","00FFC6","00FFE2","00FFFE","00E3FF",
  "00C7FF","00ABFF","008FFF","0072FF","0056FF",
  "003AFF","001DFF","0001FF","1B00FF","3800FF",
  "5400FF"]}

Map.addLayer(ph, visualization_ph, "Soil pH in H2O",0)

#Soil Organic Carbon
socc = ee.Image("OpenLandMap/SOL/SOL_ORGANIC-CARBON_USDA-6A1C_M/v02") \
  .clip(table) \
  .divide(5)

visualization_socc = {
  'bands': ['b0'],
  'min': 0.0,
  'max': 12.0,
  'palette': [
    "ffffa0","f7fcb9","d9f0a3","addd8e","78c679","41ab5d",
    "238443","005b29","004b29","012b13","00120b",
  ]}

Map.addLayer(socc, visualization_socc, "Soil organic carbon content in g / kg",0)
#%%
#Soil Bulk Density
bd = ee.Image("OpenLandMap/SOL/SOL_BULKDENS-FINEEARTH_USDA-4A1H_M/v02") \
  .clip(table) \
  .divide(10)
visualization_bd = {
  'bands': ['b0'],
  'min': 0.5,
  'max': 18.5,
  'palette': ['5e3c99', 'b2abd2', 'f7e0b2', 'fdb863', 'e63b01']
}
Map.addLayer(bd, visualization_bd, "Soil bulk density (fine earth) kg / m3",0);


#Mask mean BSI >0.01 MAY 2020 and SSM < 12 MAY 2020
mask_bsi_ssm_may = (byMonthYear.filterMetadata('month','equals',5).mosaic()).gt(0.01) \
  .And((ssm.filterDate('2020-5-1','2020-5-31').reduce(ee.Reducer.mean())).lt(12))
mask_bsi_ssm_may = mask_bsi_ssm_may.mask(mask_bsi_ssm_may)
Map.addLayer(mask_bsi_ssm_may,{'palette':'gray'},'May')

#Mask mean BSI >0.01 MAY 2020 and SSM < 12 MAY 2020, and BSI >0.01 SEP 2020 and SSM <10 SEP 2020
maskmaysep = mask_bsi_ssm_may.eq(1) \
  .And((byMonthYear.filterMetadata('month','equals',9).mosaic()).gt(0.01)) \
  .And((ssm.filterDate('2020-9-1','2020-9-30').reduce(ee.Reducer.mean())).lt(10))
maskmaysep = maskmaysep.mask(maskmaysep)
Map.addLayer(maskmaysep,{'palette':'purple'},'May+Sep')
print('maskmaysep')

#Mask mean BSI >0.01 MAY 2020 and SSM < 12 MAY 2020, and BSI >0.01 SEP 2020 and SSM <10 SEP 2020 and Soil Texture Class >6
mask_may_sep_class = maskmaysep.eq(1).And((soil_texture.select('b0')).gt(6))
mask_may_sep_class = mask_may_sep_class.mask(mask_may_sep_class)
Map.addLayer(mask_may_sep_class,{'palette':'olive'},'May+Sep+STC>6')

# %%
