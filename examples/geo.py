from iterpipe import Pipeline
from rasterstats import zonal_stats
from shapely.geometry import asShape, mapping
import click
import cligj
import json

# All functions in the pipeline
# - take a single feature as an argument
# - return a single feature

def buffer_feature(feature):
    shape = asShape(feature['geometry'])
    shape = shape.buffer(1)
    return {
        'type': 'Feature',
        'properties': feature['properties'],
        'geometry': mapping(shape)}


def zonal_srtm(feature):
    res = zonal_stats(
        feature,
        raster="/Users/mperry/data/srtm/srtm_med.tif",
        geojson_out=True)
    return res[0]


@click.command()
@cligj.features_in_arg
@click.option('--jobs', '-j', default=1)
def main(features, jobs):
    ipipe = Pipeline(buffer_feature, zonal_srtm, procs=jobs)
    for feature in ipipe(features):
        click.echo(json.dumps(feature))

if __name__ == "__main__":
    main()
