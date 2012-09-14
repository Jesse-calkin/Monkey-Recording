# Imports the monkeyrunner modules used by this program
import time
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice, MonkeyImage

resultpath = "D:\\VZ4.6\\Android\\"
refImg = MonkeyImage.loadFromFile("D:\\VZ4.6\\Android\\reference.png")

# Connects to the current device, returning a MonkeyDevice object
print "getting device..."
device = MonkeyRunner.waitForConnection()

# Installs the Android package. Notice that this method returns a boolean, so you can test
# to see if the installation worked.
#device.installPackage('myproject/bin/MyApplication.apk')

# sets a variable with the package's internal name
package = 'com.digidata.leapdrive.verizon'
print "set package " + package

# sets a variable with the name of an Activity in the package
activity = '.TeleiphoneMobileActivity'
print "set activity "+activity

# sets the name of the component to start
runComponent = package + '/' + activity


# Runs the component
print "running "+runComponent+"..."
device.startActivity(component=runComponent)

# Presses the Menu button
device.press('KEYCODE_MENU', MonkeyDevice.DOWN_AND_UP)

# Takes a screenshot
print "Grabbing screenshot..."
result = device.takeSnapshot()
filename = time.strftime("%a_%b_%Y_%H_%M_%S", ) + ".png"

# Writes the screenshot to a file
print "writing screenshot: "+filename+" to: "+resultpath 
result.writeToFile(resultpath + filename,'png')