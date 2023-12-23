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

Mobile.delay(5, FailureHandling.STOP_ON_FAILURE)

Mobile.tap(findTestObject('productPurchase/01_CariDiTokopedia'), 0)

Mobile.setText(findTestObject('productPurchase/02_CariDiTokopedia'), 'Oxihom FK9', 5)

Mobile.delay(5, FailureHandling.STOP_ON_FAILURE)

Mobile.tap(findTestObject('productPurchase/03_SearchList'), 0)

Mobile.tap(findTestObject('productPurchase/04_Product'), 0)

Mobile.tap(findTestObject('productPurchase/05_BeliLangsung'), 0)

Mobile.tap(findTestObject('productPurchase/06_BeliLangsung'), 0)

Mobile.tap(findTestObject('productPurchase/07_UbahMetodeBayar'), 0)

Mobile.tap(findTestObject('productPurchase/x_KembaliDariHalamanMetodeBayar'), 0)

Mobile.tap(findTestObject('productPurchase/07_UbahMetodeBayar'), 0)

Mobile.tap(findTestObject('productPurchase/08_Gopay'), 0)

Mobile.delay(5, FailureHandling.STOP_ON_FAILURE)

//Aquos SH-04L
//Mobile.swipe(708, 2951, 708, 1988)
//Samsung A52s
Mobile.swipe(526, 2152, 526, 700)

Mobile.tap(findTestObject('productPurchase/09_Bayar'), 0)

Mobile.setEncryptedText(findTestObject('gopay/10_PinGopay'), 'aeHFOx8jV/A=', 0)

Mobile.tap(findTestObject('gopay/11_ButtonKonfirmasi'), 0)

//belum ada step untuk input pin gopay
Mobile.tap(findTestObject('gopay/12_LihatDaftarTransaksi'), 0)

Mobile.closeApplication()

