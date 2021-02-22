import gpxpy
import gpxpy.gpx

def parse(filename):
    gpx_file = open(filename)
    gpx = gpxpy.parse(gpx_file)
    track = gpx.tracks[0]
    # Seg = track.segments
    Run = [point for segment in track.segments for point in segment.points]
    Lat = [point.latitude for point in Run]
    Lon = [point.longitude for point in Run]
    return [Lat,Lon]

def parse2(filename):
    gpx_file = open(filename)
    gpx = gpxpy.parse(gpx_file)
    track = gpx.tracks[0]
    # Seg = track.segments
    Run = [point for segment in track.segments for point in segment.points]
    Lat = [point.latitude for point in Run]
    Lon = [point.longitude for point in Run]
    coord = {"lat":Lat,"lon":Lon}
    return coord