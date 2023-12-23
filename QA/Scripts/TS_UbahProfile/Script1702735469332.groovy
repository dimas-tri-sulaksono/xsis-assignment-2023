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

// Preconditions: Start the Tokopedia application and navigate to the profile editing screen
// Start the Tokopedia application
Mobile.startExistingApplication('com.tokopedia.tkpd')

// Tap on the burger button
Mobile.tap(findTestObject('ubahProfile/btnBurger'), 0)

// Introduce a delay (for demonstration purposes)
WebUI.delay(5)

// Tap on the gear button
Mobile.tap(findTestObject('ubahProfile/btnGear'), 0)

// Tap on the pencil button
Mobile.tap(findTestObject('ubahProfile/btnPencil'), 0)

// End of Preconditions
// Test Steps: Attempt to change the profile picture with an invalid image selector
// Tap on the button to change the profile picture
Mobile.tap(findTestObject('ubahProfile/btnUbahFotoProfil'), 0)

// Handle the failure
if (Mobile.verifyElementNotExist(findTestObject('ubahProfile/selectImage'), 0, FailureHandling.OPTIONAL)) {
    // Log a message or take appropriate actions for the negative scenario
    println('Image selection failed as expected.')
} else if (Mobile.verifyElementNotExist(findTestObject('ubahProfile/warningUkuranGambarTerlaluBesar'), 0, FailureHandling.OPTIONAL)) {
	// Image size validation in gallery
	println('Image size validation appears as expected.')
} else if (Mobile.verifyElementNotExist(findTestObject('ubahProfile/warningWahUkuranGambarKebesaran'), 0, FailureHandling.OPTIONAL)) {
	println('Alert appears as expected.')
} else {
	println('Image selection succeeded, but it was expected to fail.')
}

Mobile.tap(findTestObject('ubahProfile/selectImage'), 0)

Mobile.closeApplication()

