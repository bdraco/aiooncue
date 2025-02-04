"""Onecue constants."""

from __future__ import annotations

from typing import Final

NAME_TO_SENSOR_ID: Final = {
    "Vendor": 1,
    "Controller Type": 2,
    "Current Firmware": 3,
    "Engine Speed": 4,
    "Engine Target Speed": 5,
    "Engine Oil Pressure": 6,
    "Engine Coolant Temperature": 7,
    "Battery Voltage": 11,
    "Lube Oil Temperature": 18,
    "Generator Controller Temperature": 20,
    "Engine Low Oil Pressure Switch": 26,
    "Engine Compartment Temperature": 32,
    "Engine Speed Adjustment": 33,
    "Engine Speed Gain Adjustment": 34,
    "Generator Rotation Actual": 35,
    "Generator Current Lead Lag A": 36,
    "Generator Current Lead Lag B": 37,
    "Generator Current Lead Lag C": 38,
    "Generator Current Total Lead Lag": 39,
    "Generator Power Factor A": 40,
    "Generator Power Factor B": 41,
    "Generator Power Factor C": 42,
    "Generator Total Power Factor": 43,
    "Generator Apparent Power A": 44,
    "Generator Apparent Power B": 45,
    "Generator Apparent Power C": 46,
    "Generator Total Apparent Power": 47,
    "Generator Reactive Power A": 48,
    "Generator Reactive Power B": 49,
    "Generator Reactive Power C": 50,
    "Generator Total Reactive Power": 51,
    "Generator True Power A": 52,
    "Generator True Power B": 53,
    "Generator True Power C": 54,
    "Generator True Total Power": 55,
    "Generator True Percent Of Rated Power": 56,
    "Generator Voltage AB": 57,
    "Generator Voltage BC": 58,
    "Generator Voltage CA": 59,
    "Generator Voltage Average Line To Line": 60,
    "Generator Voltage AN": 61,
    "Generator Current A": 65,
    "Generator Current B": 66,
    "Generator Current C": 67,
    "Generator Current Average": 68,
    "Generator Frequency": 69,
    "Genset Model Number Select": 91,
    "Generator Serial Number": 93,
    "Alternator Part Number -": 94,
    "Generator Controller Serial Number": 95,
    "Engine Part Number -": 96,
    "Engine Model Number": 97,
    "Engine Serial Number -": 98,
    "Generator State": 102,
    "Generator Controller Clock Time": 113,
    "Generator Controller Total Operation Time": 114,
    "Engine Total Run Time": 115,
    "Engine Total Run Time Loaded": 116,
    "Engine Total Number Of Starts": 118,
    "Genset Total Energy": 119,
    "Genset Date Time Of Last Maintenance": 121,
    "Engine Run Time At Reset Maintenance": 122,
    "Engine Run Time Until Maintenance": 123,
    "Genset Controller Hours Of Operation Since Maintenance": 124,
    "Engine Run Time Since Maintenance": 125,
    "Engine Run Time Loaded Since Maintenance": 126,
    "Engine Number Of Starts Since Maintenance": 128,
    "Genset Energy Since Maintenance": 129,
    "Genset Controller Date Format": 136,
    "Genset Controller Time Format": 137,
    "Genset Date Timeof Next Maintenance": 138,
    "Maintenance Period In Days": 139,
    "Maintenance Period Remaining": 140,
    "Genset Controller Clock Time Zone Offset": 141,
    "Ecm Model": 142,
    "Maximum Alternator Current": 143,
    "Engine Number Of Flywheel Teeth": 144,
    "Engine Warmed Up Temperature": 145,
    "Engine Cooled Down Temperature": 146,
    "Engine Crank Disconnect Speed": 147,
    "Engine Idle Speed": 148,
    "Engine Run Speed": 149,
    "Engine Coolant Temperature Protectives Enabled": 150,
    "Engine Coolant Temperature Sensor": 151,
    "Engine High Coolant Temperature Inhibit Delay": 153,
    "Engine Low Coolant Temperature Warning Delay": 154,
    "Engine High Coolant Temperature Warning Delay": 155,
    "Engine Low Coolant Temperature Shutdown Delay": 156,
    "Engine High Coolant Temperature Shutdown Delay": 157,
    "Engine Low Coolant Temperature Warning Limit": 158,
    "Engine High Coolant Temperature Warning Limit": 159,
    "Engine High Coolant Temperature Shutdown Limit": 161,
    "Engine Coolant Temperature Deadband": 162,
    "Personality Alternator Manufacturer": 163,
    "Personality Alternator Toc Time Constant": 164,
    "Personality Alternator Number Of Poles": 165,
    "Personality Alternator Type": 166,
    "Personality Fixed Voltage50 Hz": 167,
    "Personality Power Rating Single Phase50 Hz10 PF": 168,
    "Personality Power Rating Single Phase50 Hz8 PF": 169,
    "Personality Power Rating Fixed Volt50 Hz": 170,
    "Personality Power Rating50 Hz_220_440": 171,
    "Personality Power Rating50 Hz_208_415": 172,
    "Personality Power Rating50 Hz_200_400": 173,
    "Personality Power Rating50 Hz_190_380": 174,
    "Personality Power Rating50 Hz_173_346": 175,
    "Personality Power Rating50 Hz Delta": 176,
    "Personality Fixed Voltage60 Hz": 177,
    "Personality Power Rating Single Phase60 Hz10 PF": 178,
    "Personality Power Rating Single Phase60 Hz8 PF": 179,
    "Personality Power Rating Fixed Volt60 Hz": 180,
    "Personality Power Rating60 Hz_240_480": 181,
    "Personality Power Rating60 Hz_230_460": 182,
    "Personality Power Rating60 Hz_220_440": 183,
    "Personality Power Rating60 Hz_208_416": 184,
    "Personality Power Rating60 Hz_190_380": 185,
    "Personality Power Rating60 Hz Delta": 186,
    "Personality Installed Options": 188,
    "Genset System Voltage": 190,
    "Genset System Frequency": 191,
    "Genset Voltage Phase Connection": 192,
    "Genset Power Rating": 193,
    "Genset Rated Current": 194,
    "Genset System Battery Voltage": 195,
    "Prime Power Application": 196,
    "Current Transformer Ratio": 197,
    "Local Start Mode": 198,
    "Measurement System": 199,
    "Ecm Power": 200,
    "Display Contrast": 206,
    "Genset System Language": 208,
    "Genset Maximum Percent Capacity": 209,
    "Generator Overloaded Percent": 210,
    "Genset Fuel Type": 211,
    "Automatic Start Minimum Voltage": 212,
    "Automatic Stop Minimum Percent Load": 213,
    "Automatic Start Minimum Voltage Delay": 215,
    "Automatic Stop Minimum Load Delay": 216,
    "Genset Calibration Factor Voltage AB": 219,
    "Genset Calibration Factor Voltage BC": 220,
    "Genset Calibration Factor Voltage CA": 221,
    "Genset Calibration Factor Voltage AN": 222,
    "Genset Calibration Factor Current A": 225,
    "Genset Calibration Factor Current B": 226,
    "Genset Calibration Factor Current C": 227,
    "Current Transformer Calibration At No Load": 228,
    "Current Transformer Calibration At Full Load": 229,
    "Proportional Gain": 239,
    "Transient Integral Gain": 240,
    "Derivative Gain": 241,
    "Slow Correction Integral Gain": 242,
    "Diagnostic Derivative Gain": 243,
    "Diagnostic Transient Integral Gain": 244,
    "Voltage Regulator Average Voltage Adjustment": 245,
    "Voltage Regulator Volts Per Hertz Slope": 246,
    "Voltage Regulator Volts Per Hertz Cut In Frequency": 247,
    "Voltage Regulator Gain": 248,
    "Engine Start Delay": 265,
    "Engine Cool Down Delay": 267,
    "Engine Crank On Delay": 270,
    "Engine Crank Pause Delay": 271,
    "Engine Number Of Crank Cycles": 272,
    "Genset Low Battery Voltage Warning Delay": 274,
    "Genset High Battery Voltage Warning Delay": 275,
    "Genset Low Battery Voltage Warning Limit": 276,
    "Genset High Battery Voltage Warning Limit": 277,
    "Genset Battery Low Cranking Voltage Warning Delay": 278,
    "Genset Battery Low Cranking Voltage Warning Limit": 279,
    "Engine Locked Rotor Shutdown Delay": 292,
    "Genset Low Engine Speed Shutdown Limit": 294,
    "Genset High Engine Speed Shutdown Limit": 295,
    "Engine Low Oil Pressure Warning Limit": 303,
    "Engine High Oil Pressure Shutdown Limit": 306,
    "Loss Of ACSensing Shutdown Delay": 308,
    "Genset Low Voltage Shutdown Delay": 309,
    "Genset High Voltage Shutdown Delay": 310,
    "Genset Low Voltage Shutdown Limit": 311,
    "Genset High Voltage Shutdown Limit": 312,
    "Genset Short Term Low Frequency Shutdown Delay": 313,
    "Genset Long Term Low Frequency Shutdown Delay": 314,
    "Genset High Frequency Shutdown Delay": 315,
    "Genset Low Frequency Shutdown Limit": 316,
    "Genset High Frequency Shutdown Limit": 317,
    "Ats Contactor Position": 549,
    "Ats Sources Available": 550,
    "Source1 Rotation Actual": 563,
    "Source1 Voltage AB": 585,
    "Source1 Voltage BC": 586,
    "Source1 Voltage CA": 587,
    "Source1 Voltage Average Line To Line": 588,
    "Source1 Frequency": 597,
    "Source2 Rotation Actual": 598,
    "Source2 Voltage AB": 620,
    "Source2 Voltage BC": 621,
    "Source2 Voltage CA": 622,
    "Source2 Voltage Average Line To Line": 623,
    "Source2 Frequency": 632,
    "Ats Total Hours Of Operation": 661,
    "Ats Total Hours Not In Preferred": 662,
    "Ats Total Hours In Standby": 663,
    "Ats Total Switch Transfers": 664,
    "Ats Total Loss Of Preferred Transfers": 666,
    "Ats Hours Of Operation Since Maintenance": 672,
    "Ats Hours Not In Preferred Since Maintenance": 673,
    "Ats Hours In Standby Since Maintenance": 674,
    "Ats Switch Transfers Since Maintenance": 675,
    "Ats Loss Of Preferred Transfers Since Maintenance": 677,
    "Ats Source": 689,
    "Source1 System Voltage": 696,
    "Source1 System Frequency": 697,
    "Source1 Voltage Debounce Delay": 700,
    "Source1 Low Voltage Pickup": 706,
    "Source1 Low Voltage Dropout": 707,
    "Source1 Calibration Factor Voltage AB": 713,
    "Source1 Calibration Factor Voltage BC": 714,
    "Source1 Calibration Factor Voltage CA": 715,
    "Source2 System Voltage": 722,
    "Source2 System Frequency": 723,
    "Source2 Voltage Debounce Delay": 726,
    "Source2 Low Voltage Pickup": 732,
    "Source2 Low Voltage Dropout": 733,
    "Source2 Calibration Factor Voltage AB": 739,
    "Source2 Calibration Factor Voltage BC": 740,
    "Source2 Calibration Factor Voltage CA": 741,
    "Exercise Interval": 748,
    "Exercise Run Duration": 749,
    "Exercise Mode": 750,
    "Exercise Warning Enabled": 751,
    "Ats Transfer From Preferred Delay": 752,
    "Ats Transfer From Standby Delay": 753,
    "Ats Source2 Engine Start Delay": 756,
    "Is Modbus Master": 852,
    "Dhcp Enabled": 857,
    "Static IP Address": 858,
    "Static Subnet Mask": 859,
    "Static Default Gateway": 860,
    "Static Dns Server1": 861,
    "Static Dns Server2": 862,
    "Server Host Name": 863,
    "IP Address": 864,
    "Subnet Mask": 865,
    "Default Gateway": 866,
    "Dns Server1": 867,
    "Dns Server2": 868,
    "Mac Address": 869,
    "Connected Server IP Address": 870,
    "Network Connection Established": 872,
    "Media Connected": 873,
    "Rbus Active": 903,
    "Rbus Connection Count": 904,
    "Rbus Net Cycle Time": 905,
    "Rbus Timeouts": 906,
    "Rbus Errors": 907,
    "Serial Number": 908,
    "Type": 909,
    "Communication Errors": 910,
    "Communication Timeouts": 911,
    "Modbus Id": 912,
    "Last Connection Date": 913,
    "Firmware Version": 914,
    "Latest Firmware": 1671,
}
