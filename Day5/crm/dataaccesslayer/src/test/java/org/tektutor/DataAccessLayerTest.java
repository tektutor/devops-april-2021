package org.tektutor;

import org.junit.Test;
import static org.junit.Assert.*;

public class DataAccessLayerTest {

	@Test
	public void testFrontEnd() {

		DataAccessLayer dal  = new DataAccessLayer();

		String actualResponse = dal.getModuleName();
		String expectedResponse = "Data Access Layer";

		assertEquals (  expectedResponse, actualResponse );

	}

}
