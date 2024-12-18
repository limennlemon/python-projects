/*
October 21, 2023
Melanie Zwack
CMSC 115, Prof. Rowson, Week 1: Project 3
Write program that calculates/displays population at the end of each year over 5 years
(Population change variables: 1 birth every 7 seconds, 1 death every 13 seconds, 1 new immigrant every 45 seconds)
*/

public class Population {
    public static void main(String[] args) {
        // current population at start of year 1 = 312,032,486
        double popEndYr00 = 312032486; 
        
        // number of seconds in a year = 31,536,000
        double secondsPerYr = 365 * 24 * 60 * 60;
        
        // calculation of change to population each year
        double iCalcPerYr = secondsPerYr / 45;  // number of new immigrants year
        double bCalcPerYr = secondsPerYr / 7;  // number of births per year  
        double dCalcPerYr = secondsPerYr / 13;  // number of deaths per year
        double popDeltaPerYr = iCalcPerYr + bCalcPerYr - dCalcPerYr; // change to population per year
        
        // population for next 5 years based on starting population of 312,032,486
        double popEndYr01 = popEndYr00 + popDeltaPerYr;   // population after first year
        double popEndYr02 = popEndYr01 + popDeltaPerYr;   // population after second year
        double popEndYr03 = popEndYr02 + popDeltaPerYr;   // population after third year
        double popEndYr04 = popEndYr03 + popDeltaPerYr;   // population after fourth year
        double popEndYr05 = popEndYr04 + popDeltaPerYr;   // population after fifth year
        
        // print the population totals for the next five years to the screen
        System.out.println("Population total at the end of ");
        System.out.println("Year 1: " + (double)(popEndYr01));  // prints year 1 population to screen
        System.out.println("Year 2: " + (double)(popEndYr02));  // prints year 2 population to screen
        System.out.println("Year 3: " + (double)(popEndYr03));  // prints year 3 population to screen
        System.out.println("Year 4: " + (double)(popEndYr04));  // prints year 4 population to screen
        System.out.println("Year 5: " + (double)(popEndYr05));  // prints year 5 population to screen
    }
}