// This program prints all the prime numbers from 2 to n

import java.io.*;
import java.util.*;
class Solution
{
	public static void main(String args[])
	{
		Scanner sc=new Scanner(System.in);
		int n=sc.nextInt();                   //n is the number upto which we need to find the prime numbers.
	int arr[]=new int[n+1];              
	for(int i=0;i<=n;i++)                 //initialize all the indexes with 1.
	{
		arr[i]=1;
	}
	for(int i=2;(i*i)<=n;i++)                //start from 2 as 2 is the first prime number.
	{
		if(arr[i]==1)                         
		{
    
    /* replace the value at all indexes that are multiples of j with 0 
    ultimately we wiil be left with the numbers that are not multiples of any other number.*/

for(int j=i*2;j<=n;j+=i)               
		{                                         
			arr[j]=0;
		}
	}
  }
	for(int i=2;i<=n;i++)  // print the prime numbers in the range.
	{
		if(arr[i]==1)
			System.out.println(i);
	}
	}
}
