package org.tektutor;

public class  BusinessLayer  {

public static List<String> zipSlipNoncompliant(ZipFile zipFile) throws IOException {
    Enumeration<? extends ZipEntry> entries = zipFile.entries();
    List<String> filesContent = new ArrayList<>();

    while (entries.hasMoreElements()) {
      ZipEntry entry = entries.nextElement();
      File file = new File(entry.getName());
      String content = FileUtils.readFileToString(file, StandardCharsets.UTF_8); // Noncompliant
      filesContent.add(content);
    }

    return filesContent;
  }

protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws IOException {
  String name = req.getParameter("name");
  PrintWriter out = resp.getWriter();
  out.write("Hello " + name); // Noncompliant
}

	public String getModuleName()  {
		System.out.println ( "Business Layer ..." );
		return "Business Layer";	
	}


}
