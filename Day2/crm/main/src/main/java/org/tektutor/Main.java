package org.tektutor;

public class  Main  {

	public String getModuleName()  {
		return "Main Layer";	
	}

	public static void main ( String[] args )  {

		Frontend fe = new Frontend();
	        BusinessLayer bl = new BusinessLayer();	
	        DataAccessLayer dal = new DataAccessLayer();	
		
		fe.getModuleName();
		bl.getModuleName();
		dal.getModuleName();

	}

}
