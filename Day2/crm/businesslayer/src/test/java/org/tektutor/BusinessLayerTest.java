package org.tektutor;

import org.junit.Test;
import static org.junit.Assert.*;

public class BusinessLayerTest {

	@Test
	public void testFrontEnd() {

		BusinessLayer bl  = new BusinessLayer();

		String actualResponse = bl.getModuleName();
		String expectedResponse = "Business Layer";

		assertEquals (  expectedResponse, actualResponse );

	}

}
