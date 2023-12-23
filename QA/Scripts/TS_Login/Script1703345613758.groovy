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

// Pre-conditions: Delete storage and clear the cache before starting the Tokopedia application.
Mobile.startExistingApplication('com.tokopedia.tkpd', FailureHandling.STOP_ON_FAILURE)

// Close the application if it's already logged in (for demonstration purposes)
//if (Mobile.verifyElementPresent(findTestObject('loginByGoogle/btnLogout'), 5, FailureHandling.OPTIONAL)) {
//	Mobile.tap(findTestObject('loginByGoogle/btnLogout'), 0)
//}
// End of pre-conditions
// Test Steps: Google Login
Mobile.tap(findTestObject('loginByGoogle/01_Lewati'), 10, FailureHandling.OPTIONAL)

Mobile.tap(findTestObject('loginByGoogle/01b_TutupPopUp'), 10, FailureHandling.OPTIONAL)

Mobile.tap(findTestObject('loginByGoogle/02_BurgerMenu'), 0)

Mobile.tap(findTestObject('loginByGoogle/03_Masuk'), 0)

Mobile.tap(findTestObject('loginByGoogle/04_MetodeLain'), 0)

Mobile.tap(findTestObject('loginByGoogle/05_byGoogle'), 0)

Mobile.tap(findTestObject('loginByGoogle/06_Email'), 10, FailureHandling.OPTIONAL)

//Mobile.delay(5, FailureHandling.STOP_ON_FAILURE)
if (Mobile.verifyElementExist(findTestObject('loginByGoogle/06b_VerifikasiEmailCencored'), 0, FailureHandling.OPTIONAL)) {
    Mobile.tap(findTestObject('loginByGoogle/06b_VerifikasiEmailCencored'), 10, FailureHandling.OPTIONAL)

    Mobile.tap(findTestObject('loginByGoogle/06b_VerifikasiBox'), 10, FailureHandling.OPTIONAL)

    Mobile.delay(60, FailureHandling.STOP_ON_FAILURE)
}

Mobile.doubleTap(findTestObject('loginByGoogle/07_Back'), 0)

Mobile.closeApplication()
