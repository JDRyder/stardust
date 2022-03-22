
from sensirion_i2c_driver import I2cConnection
from sensirion_i2c_stc import Stc3xI2cDevice
from sensirion_i2c_stc.stc3x.data_types import Stc31BinaryGas

# Create STC3x device
#i2c_transceiver = SensorBridgeI2cProxy(bridge, port=SensorBridgePort.ONE)
stc31 = Stc3xI2cDevice(I2cConnection(i2c_transceiver))
