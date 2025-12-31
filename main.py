import sys
from airbyte_cdk.entrypoint import launch
from destination_onelake import DestinationOnelake

if __name__ == "__main__":
    # This takes the command line arguments (spec, check, write) 
    # and passes them to your Destination class.
    destination = DestinationOnelake()
    launch(destination, sys.argv[1:])