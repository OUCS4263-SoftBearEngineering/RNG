import java.io.*;
import javax.servlet.*;
import javax.servlet.http.*;
public class RandomNumGen extends HttpServlet {
    public void doGet(HttpServletRequest request, HttpServletResponse response)
    throws IOException, ServletException
    {
        int randomNumber = (int)(Math.random() * 1000000);
        response.setContentType("text/html");
        PrintWriter out = response.getWriter();
        out.println("<html>");
        out.println("<head>");
        out.println("<title>Random Number Generator</title>");
        out.println("</head>");
        out.println("<body>");
        out.println("<h1>" + randomNumber  + "</h1>");
        out.println("</body>");
        out.println("</html>");
    }
}
