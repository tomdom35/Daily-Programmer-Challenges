using System.IO;
using System;

class Program
{
    static void Main()
    {
        String line = "";
        using (StreamReader sr = new StreamReader("Fractions.txt"))
        {
            line = sr.ReadLine();
            int size = Int32.Parse(line);
            int[] fractions = new int[size*2];
            int count = 0;
            while((line = sr.ReadLine())!=null){
                int vinculumIndex = line.IndexOf("/");
                String num = line.Substring(0,vinculumIndex);
                String denom = line.Substring(vinculumIndex+1);
                int numerator = Int32.Parse(line.Substring(0,vinculumIndex));
                int denominator = Int32.Parse(line.Substring(vinculumIndex+1));
                fractions[count++] = numerator;
                fractions[count++] = denominator;
            }
            //Add all fractions together
            int[] total = addFractions(fractions[0],fractions[1],fractions[2],fractions[3]);
            count = 4;
            while(count<fractions.Length){
                total = reduce(addFractions(total[0], total[1], fractions[count++], fractions[count++]));
            }
            Console.Write(total[0]);
            Console.Write("/");
            Console.WriteLine(total[1]);
        }
    }
    //Add two fractions together. n's represent numerators. d's represent denominators
    static int[] addFractions(int n1, int d1, int n2, int d2){
        int numerator = (n1*d2) + (n2*d1);
        int denominator = d1*d2;
        int[] fraction = {numerator,denominator};
        return fraction;
    }
    //reduce the given fraction
    static int[] reduce(int[] fraction){
        int numerator = fraction[0];
        int denominator = fraction[1];
        int[] nMultiples = findMultiples(fraction[0]);
        int[] dMultiples = findMultiples(fraction[1]);
        int[] multiples = new int[nMultiples.Length];
        int count = 0;
        for(int i = 0; i<nMultiples.Length;i++){
            if(Array.IndexOf(dMultiples,nMultiples[i])!=-1){
                multiples[count++] = nMultiples[i];
            }
        }
        int gcd = findMax(multiples);
        if(gcd>1){
            numerator = numerator/gcd;
            denominator = denominator/gcd;
        }
        int[] reducedFrac = {numerator,denominator};
        return reducedFrac;
    }
    //find all multiples of a number
    static int[] findMultiples(int num){
        int multiple = 1;
        int[] multiples = new int[num];
        int multCount = 0;
        while(multiple<=num){
            if(num%multiple == 0){
                multiples[multCount++] = multiple;
            }
            multiple++;
        }
        return multiples;
    }
    //find max number in a list
    static int findMax(int[] multiples){
        int max = 0;
        for(int i = 0; i<multiples.Length; i++){
            if(max<multiples[i]){
                max = multiples[i];
            }
        }
        return max;
    }
}