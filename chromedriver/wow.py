import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.WebElement;

import com.thoughtworks.selenium.SeleneseTestCase;

public class TestCase1 extends SeleneseTestCase {
    public void setUp() throws Exception {
        login();
    }

    public void login() {
        WebDriver driver = new FirefoxDriver();
        driver.get("http://");
        WebElement id = driver.findElement(By.name("username"));
        WebElement pass = driver.findElement(By.name("password"));
        WebElement button = driver.findElement(By.xpath("/html/body/div/div/div[2]/div/form/p[3]/input"));

        id.sendKeys("tuser991@yahoo.co.in");
        pass.sendKeys("abc123");
        button.submit();
    }
}