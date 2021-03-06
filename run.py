"""Console script to launch Colorgorical.

Colorgorical can be launched through the console as either a terminal
application or as a web application built on top of a Tornado server.
"""
import argparse

from src.makeSamples import MakeSamples
import src.server as server

desc = "Colorgorical is a color palette design assistance tools to make\
        aesthetically pleasing and legible categorical color palettes for\
        information visualization."
parser = argparse.ArgumentParser(description=desc)

parser.add_argument("--server", action="store_true",
    help="Flag marking that Colorgorical should be launched as a web server.")

parser.add_argument("--makeSamples", action="store_true",
    help="Flag to create samples of 66 unique Colorgorical settings output to `samples/`.")

parser.add_argument("--port",
    help="The port to start the Colorgorical server on", default=8888)

args = parser.parse_args()

if args.server:
    s = server.ColorgoricalServer()
    portNumber = args.port if args.port else 8888
    s.start(port=portNumber)

elif args.makeSamples:
    ms = MakeSamples()
    if ms.savedResultsExist() == False:
        print 'Making palettes'
        ms.make()
    else:
        ms.loadPalettes()

    # To use Helvetica, follow the instructions below. Makes the charts look
    # a _lot_ better.
    # http://blog.olgabotvinnik.com/blog/2012/11/15/2012-11-15-how-to-set-helvetica-as-the-default-sans-serif-font-in/
    ms.savePlots()
    ms.writeTex()

else:
    print 'Did you mean to run ``python run.py --server``?'
