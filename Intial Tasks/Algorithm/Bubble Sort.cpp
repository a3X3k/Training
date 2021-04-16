#include<iostream>

using namespace std;

int main()
{
	int n,i,j;
	cout<<"Enter the Size of the Array : ";
	cin>>n;
	int arr[n];
	for(i=0;i<n;i++)
	{
		cout<<"Enter the Element "<<i+1<<" : ";
		cin>>arr[i];
	}
	cout<<"The Unsorted Array is : ";
	for(i=0;i<n;i++)
	{
		cout<<arr[i]<<" ";
	}
	for(i=0;i<n;i++)
	{
		for(j=0;j<n-i-1;j++)
		{
			if(arr[j]>arr[j+1])
			{
				int temp=arr[j+1];
				arr[j+1]=arr[j];
				arr[j]=temp;
			}
		}
	}
	cout<<"\nThe Sorted Array is : ";
	for(i=0;i<n;i++)
	{
		cout<<arr[i]<<" ";
	}
}
