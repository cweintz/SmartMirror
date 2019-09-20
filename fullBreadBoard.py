import time
import board
import busio
import adafruit_apds9960.apds9960
import adafruit_bme680
import adafruit_lsm9ds1

i2c = busio.I2C(board.SCL, board.SDA)

APDS9960 = adafruit_apds9960.apds9960.APDS9960(i2c)
APDS9960.enable_proximity = True
APDS9960.enable_color = True

BME680 = adafruit_bme680.Adafruit_BME680_I2C(i2c, debug=False)
BME680.sea_level_pressure = 1017.9

LSM9DS1 = adafruit_lsm9ds1.LSM9DS1_I2C(i2c)

while True:

    # APDS9960 stuff
    print('\nProximity: {}'.format(APDS9960.proximity()))
    r, g, b, c = APDS9960.color_data
    print('Red: {0}, Green: {1}, Blue: {2}, Clear: {3}'.format(r, g, b, c)) # unsure what c reading is

    # BME680 stuff
    print('\nTemperature: {} degrees C'.format(BME680.temperature))
    print('Gas: {} ohms'.format(BME680.gas))
    print('Humidity: {}%'.format(BME680.humidity))
    print('Pressure: {}hPa'.format(BME680.pressure))
    print("Altitude = %0.2f meters" % BME680.altitude)

    # LSM9DS1 stuff
    # Read acceleration, magnetometer, gyroscope, temperature.
    accel_x, accel_y, accel_z = LSM9DS1.acceleration
    mag_x, mag_y, mag_z = LSM9DS1.magnetic
    gyro_x, gyro_y, gyro_z = LSM9DS1.gyro
    temp = LSM9DS1.temperature
    # Print values.
    print('\nAcceleration (m/s^2): ({0:0.3f},{1:0.3f},{2:0.3f})'.format(accel_x, accel_y, accel_z))
    print('Magnetometer (gauss): ({0:0.3f},{1:0.3f},{2:0.3f})'.format(mag_x, mag_y, mag_z))
    print('Gyroscope (degrees/sec): ({0:0.3f},{1:0.3f},{2:0.3f})'.format(gyro_x, gyro_y, gyro_z))
    print('Temperature: {0:0.3f}C'.format(temp))

    time.sleep(2)
