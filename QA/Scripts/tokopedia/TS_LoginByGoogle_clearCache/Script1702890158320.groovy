import static com.kms.katalon.core.checkpoint.CheckpointFactory.findCheckpoint
import static com.kms.katalon.core.testcase.TestCaseFactory.findTestCase
import static com.kms.katalon.core.testdata.TestDataFactory.findTestData
import static com.kms.katalon.core.testobject.ObjectRepository.findTestObject
import static com.kms.katalon.core.testobject.ObjectRepository.findWindowsObject
import com.kms.katalon.core.checkpoint.Checkpoint as Checkpoint
import com.kms.katalon.core.cucumber.keyword.CucumberBuiltinKeywords as CucumberKW
import com.kms.katalon.core.mobile.keyword.MobileBuiltInKeywords as Mobile
import com.kms.katalon.core.model.FailureHandling as FailureHandling
import com.kms.katalon.core.testcase.TestCase as TestCase
import com.kms.katalon.core.testdata.TestData as TestData
import com.kms.katalon.core.testng.keyword.TestNGBuiltinKeywords as TestNGKW
import com.kms.katalon.core.testobject.TestObject as TestObject
import com.kms.katalon.core.webservice.keyword.WSBuiltInKeywords as WS
import com.kms.katalon.core.webui.keyword.WebUiBuiltInKeywords as WebUI
import com.kms.katalon.core.windows.keyword.WindowsBuiltinKeywords as Windows
import internal.GlobalVariable as GlobalVariable
import org.openqa.selenium.Keys as Keys

Mobile.startExistingApplication('com.tokopedia.tkpd', FailureHandling.STOP_ON_FAILURE)

Mobile.tap(findTestObject('tokopedia/loginByGoogleNewDevice/btnLewati'), 0)

Mobile.tap(findTestObject('tokopedia/loginByGoogleNewDevice/btnTutupPopUp'), 0)

Mobile.tap(findTestObject('tokopedia/loginByGoogleNewDevice/btnBurger'), 0)

Mobile.tap(findTestObject('tokopedia/loginByGoogleNewDevice/btnMasukMenuUtama'), 0)

Mobile.tap(findTestObject('tokopedia/loginByGoogleNewDevice/btnMetodeLain'), 0)

Mobile.tap(findTestObject('tokopedia/loginByGoogleNewDevice/btnGoogle'), 0)

Mobile.tap(findTestObject('tokopedia/loginByGoogleNewDevice/btnAkunLinear'), 0)

Mobile.closeApplication()

