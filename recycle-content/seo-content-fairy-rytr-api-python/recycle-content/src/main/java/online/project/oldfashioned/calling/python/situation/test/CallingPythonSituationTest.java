/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Project/Maven2/JavaApp/src/main/java/${packagePath}/${mainClassName}.java to edit this template
 */
package online.project.oldfashioned.calling.python.situation.test;

import java.io.IOException;
import jep.Interpreter;
import jep.JepException;
import jep.SharedInterpreter;

/**
 *
 * @author valorantdigital
 */
public class CallingPythonSituationTest {

    public static void main(String[] args) throws IOException, InterruptedException {
        System.out.println("Hsa");

        Process p = new ProcessBuilder("python", "source-code/app.py")
                .redirectErrorStream(true)
                .start();
        p.getInputStream().transferTo(System.out);
        int rc = p.waitFor();

        System.out.println("rc: " + rc);
    }

    public String sayHello(String name) {
        try ( Interpreter interp = new SharedInterpreter()) {
            interp.set("user_name", name);
            interp.exec("result = 'Hi, ' + user_name");
            String output = (String) interp.getValue("result");
            return output;
        } catch (JepException e) {
            //do something with exception
            return null;
        }
    }
}
