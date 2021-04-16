#include<iostream>

using namespace std;

int merge(int arr[],int start,int end,int key)
{
	if(start<=end)
	{
		int mid=(start+end)/2;
		if(arr[mid]==key)
		{
			cout<<"\nThe Element is Found";
			return 0;
		}
		else if(key<arr[mid])
		{
			return merge(arr,start,mid-1,key);
		}
		else
		{
			return merge(arr,mid+1,end,key);
		}
	}
	else
	{
		cout<<"\nThe Element is Not Found";
		return 0;
	}
}

int main()
{
	int n,i,j,key;
	cout<<"Enter the Size of the Array : ";
	cin>>n;
	int arr[n];
	for(i=0;i<n;i++)
	{
		cout<<"Enter the Element "<<i+1<<" : ";
		cin>>arr[i];
	}
	cout<<"The Sorted Array is : ";
	for(i=0;i<n;i++)
	{
		cout<<arr[i]<<" ";
	}
	cout<<"\nEnter the Element you want to Search : ";
	cin>>key;
	merge(arr,0,n,key);
	return 0;
}
