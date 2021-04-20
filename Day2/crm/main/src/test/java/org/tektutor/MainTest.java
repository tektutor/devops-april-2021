package org.tektutor;

import org.junit.Test;
import static org.junit.Assert.*;

public class MainTest {

	@Test
	public void testFrontEnd() {

		Main mainObj  = new Main();

		String actualResponse = mainObj.getModuleName();
		String expectedResponse = "Main Layer";

		assertEquals (  expectedResponse, actualResponse );

	}

}
