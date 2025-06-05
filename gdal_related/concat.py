from osgeo import gdal
import numpy as np


# 'orienation' - true: vertical, false: horizontal
def concat(orientation, tif1, tif2, outputName):
    print(f'Concatenating {tif1} with {tif2} to {outputName}...', end='\r', flush=True)

    # Open first image
    ds1 = gdal.Open(tif1)
    band1_1 = ds1.GetRasterBand(1).ReadAsArray()

    # Open second image
    ds2 = gdal.Open(tif2)
    band2_1 = ds2.GetRasterBand(1).ReadAsArray()

    # Check dimensions
    assert band1_1.shape == band2_1.shape, "Input images must be the same size"

    # Concatenate method
    if orientation:
        concatenated = np.vstack((band1_1, band2_1))
    else:
        concatenated = np.hstack((band1_1, band2_1))

    # Create output raster
    driver = gdal.GetDriverByName('GTiff')
    rows, cols = concatenated.shape
    out_ds = driver.Create(outputName, cols, rows, 1, gdal.GDT_Int16)

    # Set geotransform and projection from one of the inputs if needed
    out_ds.SetGeoTransform(ds1.GetGeoTransform())
    out_ds.SetProjection(ds1.GetProjection())

    # Write data
    out_ds.GetRasterBand(1).WriteArray(concatenated)

    # Close datasets
    ds1 = None
    ds2 = None
    out_ds = None

    print(f'Concatenating {tif1} with {tif2} to {outputName} Done')

if __name__ == '__main__':
    vertical = [('A1.tif', 'A2.tif'), ('B1.tif', 'B2.tif'), ('C1.tif', 'C2.tif'), ('D1.tif', 'D2.tif')]

    for pair in vertical:
        concat(True, pair[0], pair[1], f'{pair[0][0]}.tif')

    concat(False, 'A.tif', 'B.tif', 'west.tif')
    concat(False, 'C.tif', 'D.tif', 'east.tif')

