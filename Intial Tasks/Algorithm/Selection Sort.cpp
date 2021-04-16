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
		int min=i;
		for(j=i+1;j<n;j++)
		{
			if(arr[j]<arr[min])
			{
				min=j;
			}
		}
		int temp=arr[i];
		arr[i]=arr[min];
		arr[min]=temp;
	}
	cout<<"\nThe Sorted Array is : ";
	for(i=0;i<n;i++)
	{
		cout<<arr[i]<<" ";
	}
}
