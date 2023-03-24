import java.util.*;
import javax.swing.*;
public class Voter {
    static  ArrayList<String> Password = new ArrayList<>();
    static  ArrayList<String> Username = new ArrayList<>();
    static void vote(String username,String password) {
        for(int k=0;k<=15;k++){
        if (username.equals(Username.get(k)) && password.equals(Password.get(k))) {
            count= true;
            option = JOptionPane.showInputDialog("Select an option \n 1. Vote\n 2. Check Eligibility\n 3. Cancel");

            switch (option) {

                case "1":
                    JOptionPane.showMessageDialog(null, "You have 5 choices\n1. Imran\n2. Attiq\n3. Ali Zohaib\n4. Hifzur Rehman\n5. Aliya Razia\nRate Each One out of 5 ");
                    I = Integer.parseInt(JOptionPane.showInputDialog("Rate Imran (1-5)"));
                    Im = Im + I;
                    A = Integer.parseInt(JOptionPane.showInputDialog("Rate Attiq (1-5)"));

                    At = At + A;
                    Z = Integer.parseInt(JOptionPane.showInputDialog("Rate Ali-Zohaib (1-5)"));

                    AZ = AZ + Z;
                    H = Integer.parseInt(JOptionPane.showInputDialog("Rate Hifzur Rehman (1-5)"));

                    HR = HR + H;
                    R = Integer.parseInt(JOptionPane.showInputDialog("Rate Aliya Razia (1-5)"));
                    AR = AZ + R;
                    break;
                case "2":
                    try {
                        Voter.Eligible();
                    } catch (Exception e) {
                        e.printStackTrace();
                    }
                    break;
                default:
                    System.out.println("");
                    break;

            }
        }
           if(count==true){
               System.out.println("1");
                break;}
        }}
        static int b, c, d, x;

        static char[] Cnic;

        static void inputmethod () {
            boolean checkCNIC = false;
            while (checkCNIC == false) {
                Scanner sc = new Scanner(System.in);

                String cnic = JOptionPane.showInputDialog("Enter your Cnic Number\n(only Punjab)");
                if (cnic.length() != 13) {
                    JOptionPane.showMessageDialog(null, "Enter 13 digits only!!", "Alert", JOptionPane.ERROR_MESSAGE);

                } else {

                    checkCNIC = true;
                    Cnic = cnic.toCharArray();
                }
            }

            for (int i = 0; i < 13; i++) {

                if (Character.isDigit(Cnic[i])) {
                    switch (i) {
                        case 0: {
                            b = Integer.parseInt(String.valueOf(Cnic[i]));
                            break;
                        }

                        case 1: {
                            c = Integer.parseInt(String.valueOf(Cnic[i]));
                            break;
                        }

                        case 12: {
                            d = Integer.parseInt(String.valueOf(Cnic[i]));
                            break;
                        }

                        default:
                            System.out.print("");

                            break;
                    }
                } else {
                    JOptionPane.showMessageDialog(null, "Enter Digits only!!", "Alerts", JOptionPane.ERROR_MESSAGE);

                    inputmethod();
                    break;
                }

            }
        }

    static void Eligible() {


        inputmethod();

        if (d % 2 == 0) {
           JOptionPane.showMessageDialog(null,"Age: <18\nYour are NOT Eligible to Vote!!","Alerts",JOptionPane.ERROR_MESSAGE);

        }

        else if (b == 3 && c == 0 && d % 2 == 1) {
           JOptionPane.showMessageDialog(null,"Province: PUNJAB\nDivision:  BHAWALPUR\nAge: 18+\nYour are Eligible to Vote!!","Info",JOptionPane.INFORMATION_MESSAGE);

        }

        else if (b == 3 && c == 1 && d % 2 == 1) {
           JOptionPane.showMessageDialog(null,"Province: PUNJAB\nDivision:  MULTAN\nAge: 18+\nYour are Eligible to Vote!!","Info",JOptionPane.INFORMATION_MESSAGE);

        }

        else if (b == 3 && c == 2 && d % 2 == 1) {
           JOptionPane.showMessageDialog(null,"Province: PUNJAB\nDivision:  Dera Ghazi Khan\nAge: 18+\nYour are Eligible to Vote!!","Info",JOptionPane.INFORMATION_MESSAGE);

        }

        else if (b == 3 && c == 3 && d % 2 == 1) {
            JOptionPane.showMessageDialog(null,"Province: PUNJAB\nDivision:  FAISALABAD\nAge: 18+\nYour are Eligible to Vote!!","Info",JOptionPane.INFORMATION_MESSAGE);

        }

        else if (b == 3 && c == 4 && d % 2 == 1) {
            JOptionPane.showMessageDialog(null,"Province: PUNJAB\nDivision:  GUJRANWALA\nAge: 18+\nYour are Eligible to Vote!!","Info",JOptionPane.INFORMATION_MESSAGE);

        }

        else if (b == 3 && c == 5 && d % 2 == 1) {
            JOptionPane.showMessageDialog(null,"Province: PUNJAB\nDivision:  LAHORE\nAge: 18+\nYour are Eligible to Vote!!","Info",JOptionPane.INFORMATION_MESSAGE);

        }

        else if (b == 3 && c == 6 && d % 2 == 1) {
            JOptionPane.showMessageDialog(null,"Province: PUNJAB\nDivision:  SAHIWAL\nAge: 18+\nYour are Eligible to Vote!!","Info",JOptionPane.INFORMATION_MESSAGE);

        }

        else if (b == 3 && c == 7 && d % 2 == 1) {
           JOptionPane.showMessageDialog(null,"Province: PUNJAB\nDivision:  RAWALPINDI\nAge: 18+\nYour are Eligible to Vote!!","Info",JOptionPane.INFORMATION_MESSAGE);

        }

        else if (b == 3 && c == 8 && d % 2 == 1) {
           JOptionPane.showMessageDialog(null,"Province: PUNJAB\nDivision:  SARGODHA\nAge: 18+\nYour are Eligible to Vote!!","Info",JOptionPane.INFORMATION_MESSAGE);

        }

    }
    static boolean count=false;

    static int age, noc,  choice,  Im, At, AZ, HR, AR, a, I, A, Z, R, H, n;

    static String Nov, aov, Option, username12, password12,option,select;

    static double cnic;

    static String[] username1;

    static String[] password1;


    public static void main(String[] args) {

        Password.add("danial123");
        Password.add("ahmed123");
        Password.add("nadeem123");
        Password.add("abdullah123");
        Password.add("hashim123");
        Password.add("talha123");
        Password.add("zohaib123");
        Password.add("jawad123");
        Password.add("zeeshan123");
        Password.add("noor123");


        Username.add("danial");
        Username.add("ahmed");
        Username.add("nadeem");
        Username.add("abdullah");
        Username.add("hashim");
        Username.add("talha");
        Username.add("zohaib");
        Username.add("jawad");
        Username.add("zeeshan");
        Username.add("noor");
       JOptionPane.showMessageDialog(null,"      Automatic Voting System","Welcome",JOptionPane.PLAIN_MESSAGE);


        Scanner sc = new Scanner(System.in);

        for (int i = 0; i <= 15; i++) {

               select= JOptionPane.showInputDialog(null,"Select an option\n 1.Voter\n 2.Admin\n 3.Cancel");



                switch(select){

      case "1": {
                    for(int z=0;z<4;z++){

                   String username=JOptionPane.showInputDialog("Voters Interface\n\nEnter username","username");

                    String password =JOptionPane.showInputDialog("Enter password: ","password");

                             vote(username,password);
                        if (count==true) {
                            System.out.println("2");
                            break;
                        }
                        else {
                            JOptionPane.showMessageDialog(null,"Entered username/password is wrong\nPlease try again","Oops",JOptionPane.ERROR_MESSAGE);}
                    }
                    break;}

    case "2": {
                    JOptionPane.showMessageDialog(null,"Enter Username Password","Management Interface",JOptionPane.PLAIN_MESSAGE);

                    username12 = JOptionPane.showInputDialog("Enter username ");

                    password12 = JOptionPane.showInputDialog("Enter password ");

                    if ("admin".equals(username12) && "admin@123".equals(password12)) {

                       int o=Integer.parseInt(JOptionPane.showInputDialog("1. Add Voter \n2. Check result\n3. Cancel"));
                        switch(o){

                            case 1:
                        n = Integer.parseInt(JOptionPane.showInputDialog("Enter Number of Voters you want to add:"));

                        for (int s = 10; s < (10 + n); s++) {
                           JOptionPane.showMessageDialog(null,"   Add Voter ");

                            String w = JOptionPane.showInputDialog("Enter username ");

                            Password.add(s, w);

                            String b = JOptionPane.showInputDialog("Enter password ");

                            Username.add(i, b);

                        }
                            break;

                            case 2:
                                if (Im > At && Im > AZ && Im > HR && Im > AR) {
                                    JOptionPane.showMessageDialog(null,"    IMRAN HAS WON \n   Points earned"+Im,"Congratultions!",JOptionPane.WARNING_MESSAGE);
                                }

                                else if (At > Im && At > AZ && At > HR && At > AR) {
                                    JOptionPane.showMessageDialog(null,"   ATTIQ HAS WON  \n   Points earned  "+ At ,"Congratultions!",JOptionPane.WARNING_MESSAGE);
                                }

                                else if (AZ > Im && AZ > At && AZ > HR && AZ > AR) {
                                    JOptionPane.showMessageDialog(null,"   ALI ZOHAIB HAS WON  \n   Points earned  "+ AZ ,"Congratultions!",JOptionPane.WARNING_MESSAGE);
                                }

                                else if (HR > Im && HR > At && HR > AR && HR > AZ) {
                                    JOptionPane.showMessageDialog(null,"   HIFZUR_REHMAN HAS WON  \n   Points earned  "+ HR ,"Congratultions!",JOptionPane.WARNING_MESSAGE);
                                }

                                else if (AR > Im && AR > HR && AR > At && AR > AZ) {
                                    JOptionPane.showMessageDialog(null,"   ALIYA RAZIA HAS WON  \n   Points earned  "+ AR ,"Congratultions!",JOptionPane.WARNING_MESSAGE);
                                }
                                else{
                                    JOptionPane.showMessageDialog(null,"No winners yet","Winner",JOptionPane.INFORMATION_MESSAGE);
                                }


                            break;

                            case 3:{
                                break;
                            } }}

                    else {

                       JOptionPane.showMessageDialog(null,"Entered username/password is wrong\nPlease try again","Oops",JOptionPane.ERROR_MESSAGE);
                    }
                }

                    case "3":
                        break; }
            if(option=="3"){
                break;
            }
        }
        sc.close();
        sc.close();
    }
}
