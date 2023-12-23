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

Mobile.tap(findTestObject('signUp/03_Daftar'), 0)

Mobile.tap(findTestObject('signUp/04_IzinkanTelepon'), 10, FailureHandling.OPTIONAL)

Mobile.tap(findTestObject('signUp/05a_EmailAtauNomorPonsel'), 10, FailureHandling.OPTIONAL)

Mobile.setText(findTestObject('signUp/05a_EmailAtauNomorPonsel'), 'rayaco7955@vkr1.com', 10, FailureHandling.OPTIONAL)

Mobile.tap(findTestObject('signUp/05b_EmailAtauNomorPonsel'), 10, FailureHandling.OPTIONAL)

Mobile.setText(findTestObject('signUp/05b_EmailAtauNomorPonsel'), 'rayaco7955@vkr1.com', 10, FailureHandling.OPTIONAL)

Mobile.tap(findTestObject('signUp/05c_EmailatauNomorPonsel2'), 10, FailureHandling.OPTIONAL)

Mobile.setText(findTestObject('signUp/05c_EmailatauNomorPonsel2'), 'rayaco7955@vkr1.com', 10, FailureHandling.OPTIONAL)

Mobile.tap(findTestObject('signUp/06a_Daftar'), 10, FailureHandling.OPTIONAL)

Mobile.tap(findTestObject('signUp/06b_lanjut'), 10, FailureHandling.OPTIONAL)

Mobile.tap(findTestObject('signUp/07_VerifikasiEmail'), 10, FailureHandling.OPTIONAL)

Mobile.delay(60, FailureHandling.STOP_ON_FAILURE)

Mobile.tap(findTestObject('signUp/z_NamaLengkap'), 0)

Mobile.setText(findTestObject('signUp/z_NamaLengkap'), 'Muhammad', 0, FailureHandling.OPTIONAL)

Mobile.tap(findTestObject('signUp/z_KataSandi'), 0)

Mobile.setText(findTestObject('signUp/z_KataSandi'), 'password', 0, FailureHandling.OPTIONAL)

Mobile.closeApplication()

