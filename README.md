# auto_phone

#### allure generate result -o report --clean

#### console: pytest --reruns=1 --reruns-delay=2 --alluredir result

/Users/xiaoqiang/Downloads/sdk/build-tools/30.0.3/aapt dump badging xxx.apk

```angular2html
安装android sdk，xcode
配置ANDROID_HOME
brew install libimobiledevice --HEAD
brew install carthage
brew install node
npm install -g appium
npm install wd
npm install -g ios-deploy
gem install xcpretty  # optional
appium
```

```angular2html
/opt/homebrew/Cellar/ios-deploy/1.11.4/bin
```

#### ios 真机运行

```
配置WebDriverAgent
https://github.com/facebookarchive/WebDriverAgent
运行初始化脚本
用xcode打开 WebDriverAgent.xcodeproj
WebDriverAgentLib-->Signing & capablities-->勾选Automatically manage signing-->选择team
    Build Settings-->Build active Architecture Only-->No --->>Linking-->Runpath Search Paths-->$(SRCROOT)/../Carthage/Build/iOS,$(PROJECT)/Carthage/Build/iOS
    Packing -->Product Bundle Identifier --> com.trip.WebDriverAgentLib
WebDriverAgentRunner-->Signing & Capablities -->勾选Automatically manage signing-->选择team
Product --> Destination --> real device
Product --> Scheme -->WebDriverAgentRunner
Product --> Test
```

```angular2html
  "platformName": "ios",
"platformVersion": "14.7",
"udid": "00008030-000A108A3AA0802E",
"deviceName": "iPhone 11 pro",
"automationName": "XCUITest",
"bundleid": "com.trip.WebDriverAgentLib",
"xcodeOrgid": "weiqiang.liu@qunar.com",
"xcodeSigningId": "iPhone Developer"
```
```angular2html
如果报错找不到xcode，执行如下操作，最后边是xcode的安装路径
sudo xcode-select --switch /Applications/Xcode.app
```