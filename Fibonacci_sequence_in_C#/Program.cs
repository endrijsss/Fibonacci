using System;

namespace Fibonacci
{
    class Program
    {
        static long a = 0, b =1, c;
        static void Main(string[] args)
        {
            Console.WriteLine("How many Fibonacci sequence numbers you want to display?:");
            long count= Int64.Parse( Console.ReadLine());
            
            Console.Write(a + " " + b );
            for(long i=2;i<count;i++)
            {
                c = a + b;
                Console.Write(" " + c);
                a = b;
                b = c;
            }
            Console.WriteLine();
        }
    }
}