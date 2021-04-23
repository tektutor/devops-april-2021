package org.tektutor;
import java.utils.logging.*;

public class  Frontend  {

	public String getModuleName()  {
		//System.err.println ( "FrontEnd  Layer ..." );

		Logger logger = Logger.getLogger ( GFG.class.getName() );
		logger.log ( Level.INFO, "Entered getModuleName method ..." );
		logger.log ( Level.WARNING, "This is a warning mmessage." );
		

		return "Frontend Layer";	
	}


}
