package org.tektutor;

import org.junit.Test;
import static org.junit.Assert.*;

public class FrontendTest {

	@Test
	public void testFrontEnd() {

		Frontend fe  = new Frontend();

		String actualResponse = fe.getModuleName();
		String expectedResponse = "Frontend Layer";

		assertEquals (  expectedResponse, actualResponse );

	}

}
