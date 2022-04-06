from main import GetConfig
import datetime as dt

# Generate configuration object
configuration        = GetConfig('config.cfg')

# Load project settings
settings             = configuration.settings    

# Load project sections
planned_section      = configuration.planned
accomplished_section = configuration.accomplished
replanned_section    = configuration.replanned

# Get values
planned_values       = configuration.get_values(planned_section)
accomplished_values  = configuration.get_values(accomplished_section)
replanned_values     = configuration.get_values(replanned_section)

if __name__ == '__main__':
    print(planned_values)
    print(accomplished_values)
    print(replanned_values)