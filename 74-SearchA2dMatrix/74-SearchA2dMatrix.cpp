// Last updated: 1/2/2026, 12:18:48 PM
class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int row =matrix.size();
        int column= matrix[0].size();
        int start =0;
        int end =row*column-1;
        int mid =start +(end -start /2);

    while (start <=end )
    {
        int element =matrix [mid/column][mid %column];
        if (element ==target )
        {
            return 1 ;
        }
        if (element <target )
        {
           start=mid+1;
        }
        if (element >target )
        {
            end =mid-1;

        }

        mid =start +(end-start/2);
    }
    return 0;
    }
    
};