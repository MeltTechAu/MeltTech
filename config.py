import logging
########################################################################
########################################################################
########################################################################
#   MeltTech Comes Set up For Kilns Just Auto Tune and paste PID parameters below as per instructions "no commers","
#   General options
#
#   Below is the The PID settings. Autotune your kiln from cold then put figures from Terminal Results into below kp,ki,kd below and save
#   #Default=kp1.0,ki0.0,kd0.0
#
#   PID parameters

pid_kp = 1.0  # Proportional   #Enter P Results From Terminal here after Auto Tune See Manual     Default=1.0
pid_ki = 0.0  # Integration    #Enter I Results From Terminal here after Auto Tune See Manual     Default=0.0
pid_kd = 0.0  # Derivative     #Enter D Results From Terminal here after Auto Tune See Manual     Default=0.0

########################################################################
tune_target_temp = 500         #Enter your required Tuning temperature here #Default=500
tune_cycles = 8                #Enter amount of tuning cycles here #Default=8

emergency_shutoff_temp = 1305  #Put in a High Limit Onced reached it stops program and heat is turned off #Default=1305
thermocouple_offset = 0        #For adjusting an Thermocouple offset if calibration is out #Default=0
bung_temp = 700                #For Kilns to remind you to put your Bungs into your kiln currently only logs in Terminal in manual mode only atm Push to Screen Warning #Default=700

### Cost Estimate
kwh_rate        = 0.30  # Rate in currency_type to calculate cost to run job
currency_type   = "AUD"   # Currency Symbol to show when calculating cost to run job
oven_power      = 4800  # Average watts consumed by oven while running set for single phase 20Amp
#Oven power cost calculations must be change currently in /home/YourComputerName/MeltTech/public/assets/js/picoreflow.js File open with mousepad/text editor


########################################################################
########################################################################
########################################################################


#######EVERY THING BELOW LEAVE AS IS!!!!!!YOU ARE NOW READY TO TUNE YOUR KILN ONCE SETTINGS ARE ADJUSTED IF NEEDED ABOVE Tune your kiln!!!
#As MeltTech uses mechanical relays don't set less then 14 seconds or you will damage the controller and shorten it's life

# PWM Settings
### Default period of PWM, in seconds adjust this for more response if needed #Default=14
PWM_Period_s = 14

# The period will be extended to meet the demanded duty cycle for DC close to 0 or 100%
# without violating the minimum on/off time, until the period reaches its max, at which point
# the system will go full off or on
# This allows more precise PWM near 0 or 1 without causing rapid relay switching

### Minimum On or Off time, in seconds. #Default=14
PWM_MinimumOnOff_s = 14

### Maximum allowed extended period
PWM_PeriodMax_s = 90

### Logging
log_level = logging.INFO
log_format = '%(asctime)s %(levelname)s %(name)s: %(message)s'

### Server
listening_ip = "0.0.0.0"
listening_port = 8081



########################################################################
### Thermocouple SPI Connection (using adafrut drivers + kernel SPI interface)
spi_sensor_chip_id = 0

### Amount of time, in seconds, to wait between reads of the thermocouple
sensor_read_period = 1
########################################################################

#   Time and Temperature parameters

## These are defaults for new profiles, and can be modified on a per-profile basis edit files with text editor located in storage/profiles directory

# some functions below are work in progress currently All set only for time in minutes especially costings leave alone.

temp_scale          = "c" # c = Celsius | f = Fahrenheit - Unit to display 
time_scale_slope    = "m" # s = Seconds | m = Minutes | h = Hours - Slope displayed in temp_scale per time_scale_slope
time_scale_profile  = "m" # s = Seconds | m = Minutes | h = Hours - Enter and view target time in time_scale_profile

# PWM Offset Adjustment 
# For systems with multiple heaters and uneven heating, these factors will adjust the PWM to compensate
# For instance, if heater 1 needs to be on more often than heater 2, make heat1adj positive and heat2adj negative

heat1adj = 0		# heater 1 PWM offset, in percent  Default=0
heat2adj = 0		# heater 2 PWM offset, in percent  Default=0

##Enabled outputs
heat_enabled = True		# Enable control for heater Default=True
heat2_enabled = True	# Enabled control for second heater Leave as true still working on this Default=True
cool_enabled = False	# Enable control for cooler (exterior fan, etc.) Default=False
air_enabled = False		# Enable control for internal air circulation (interior fan) Default=False

### Outputs
gpio_heat = 20  # Switches zero-cross solid-state-relay Default=20
gpio_heat2 = 5 # Second heater control Default=5
gpio_cool = 21  # Regulates PWM for 12V DC Blower Default=21
gpio_air  = 16   # Switches 0-phase det. solid-state-relay Default=16
gpio_beeper = 6  # Switches beeper Default=6

heater_invert = 0 # switches the polarity of the heater control 0 for SSR Heat 1 for Relay Default=0

### Inputs
door_enabled = False	# Enable sensor for door open Default=False
gpio_door = 18 #Default=18

### Thermocouple Adapter selection:
#   max31855 - bitbang SPI interface
#   max31855spi - kernel SPI interface
#   max6675 - bitbang SPI interface
max31855 = 1 #Default=1
max6675 = 0 #Default=1
max31855spi = 0 # Consumes pins 7,8,9,10,11

### Thermocouple Connection (using bitbang interfaces)
gpio_sensor_cs = 19     #Default=19
gpio_sensor_clock = 13  #Default=13
gpio_sensor_data = 26   #Default=26

### Profile Adjustments for Kilns currently not Working leave below must hit temp and cone slope adjust as is working on it.
# must_hit_temp adjusts for systems where the heater might not be able to keep up with the profile
# If false, the system will not adjust the timing of the profile
# If true, the system is guaranteed to hit the temperatures of the profile. It will wait until
# the target is reached before moving to the next segment of the profile
must_hit_temp = False   #Default=False
### Profile Adjustments for Kilns currently not working leave below must hit temp and cone slope adjust as is working on it.
# Cone slope adj adjusts the target temperature when the segment takes longer than expected
# It's expressed in deg C per (deg C per hour), i.e. the shift in temperature target per shift in temperature rate
# For instance, setting to 0.4 will reduce the target temperature by 40 deg C if the final slope is 100 deg C/hour
# lower than the profile slope
# Only used if must_hit_temp is True
cone_slope_adj = 0.0   #Default=0.0

######################################################################## DO NOT USE YET!!!! if no WIFI kiln either goes Full On or Full OFF
#   Logging parameters leave below as is at moment use live graph :)
logging_time_step = 60.0 # seconds between logging
#ubidots_url = 'https://things.ubidots.com/api/v1.6/devices/NemesisPI/'
#ubidots_token = "your token here"

#   Simulation parameters
sim_t_env      = 25.0   # deg C
sim_c_heat     = 100.0  # J/K  heat capacity of heat element
sim_c_oven     = 2000.0 # J/K  heat capacity of oven
sim_p_heat     = 3500.0 # W    heating power of oven
sim_R_o_nocool = 1.0    # K/W  thermal resistance oven -> environment
sim_R_o_cool   = 0.05   # K/W  " with cooling
sim_R_ho_noair = 0.1    # K/W  thermal resistance heat element -> oven
sim_R_ho_air   = 0.05   # K/W  " with internal air circulation

#2022 BP
