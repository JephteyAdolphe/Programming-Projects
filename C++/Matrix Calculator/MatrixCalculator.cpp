#include <iostream>
#include <string>
#include <stdio.h>
using namespace std;

int rows1, rows2, columns1, columns2, choice, i, j, ev;
int mat1[10][10];
int mat2[10][10];

int addition();
int subtraction();
int multiplication();
int determinant();
int transpose();
int inverse();
void display1(int* rows1, int* columns1);
void display2(int* rows2, int* columns2);

int main()
{
    
    
    cout << "Menu\nChoice 1: addition\nChoice 2: subtraction\nChoice 3: multiplication\nChoice 4: determinant\nChoice 5: transpose\nChoice 6: inverse\nChoice 0: exit\n\n";
    cout << "Enter your choice: ";
    cin >> choice; // matrix operator
    
    if(choice>6 || choice<0){
    cout << "Invalid Operation!";
    return 0;
    }
    
    // Switch Case Code
    switch (choice)
    {
        case 1: addition();
            break;
        case 2: subtraction();
            break;
        case 3: multiplication();
            break;
        case 4: determinant();
            break;
        case 5: transpose();
            break;
        case 6: inverse();
            break;
        case 0: return 0;
            break;
    }
    
    return 0;
}


int addition(){
    
    int m, n, addMat[10][10];
    
      // Set bounds for matrix
    cout << "matrix1 # of rows: ";
    cin >> rows1;
    cout << "matrix1 # of columns: ";
    cin >> columns1;
    
    int* ptrRow1 = &rows1;
    int* ptrColumn1 = &columns1;
    
    if(columns1>10 || rows1>10 || columns1<1 || rows1<1)
    return 0;
    
    
    
    for(i=0;i<rows1;i++){
        for(j=0;j<columns1;j++){
            
            cout << "Enter element (" << i << "," << j << "): ";
            cin >> ev; // elemtent value
            mat1[i][j] = ev;
        }
        
    }
    
    display1(ptrRow1, ptrColumn1);
    // Get elements to display as a whole after mat1 loop
    
    cout << "matrix2 # of rows: ";
    cin >> rows2;
    cout << "matrix2 # of columns: ";
    cin >> columns2;
    
    int* ptrRow2 = &rows2;
    int* ptrColumn2 = &columns2;
    
    if(columns1>10 || rows1>10 || columns1<1 || rows1<1)
    return 0;
    
     if((rows2 != rows1) || (columns2 != columns1)){
    cout << "Operation is not supported";
    return 0;   
    }
    
    for(i=0;i<rows2;i++){
        for(j=0;j<columns2;j++){
            
            cout << "Enter element (" << i << "," << j << "): ";
            cin >> ev; // elemtent value
            mat2[i][j] = ev;
        }
        
    }
    
    display2(ptrRow2, ptrColumn2);
    // Get elements to display as a whole after mat2 loop
    
   
    
    
    for(m=0;m<rows1;m++){
        for(n=0;n<columns1;n++){
            
            addMat[m][n] = mat1[m][n] + mat2[m][n];
            cout << addMat[m][n] << " ";
        }
        cout << endl;
    }
        
    main();
}


int subtraction(){
    
    int m, n, subMat[10][10];
    
      // Set bounds for matrix
    cout << "matrix1 # of rows: ";
    cin >> rows1;
    cout << "matrix1 # of columns: ";
    cin >> columns1;
    
    if(columns1>10 || rows1>10 || columns1<1 || rows1<1)
    return 0;
    
    
    
    for(i=0;i<rows1;i++){
        for(j=0;j<columns1;j++){
            
            cout << "Enter element (" << i << "," << j << "): ";
            cin >> ev; // elemtent value
            mat1[i][j] = ev;
        }
        
    }
    
    int* ptrRow1 = &rows1;
    int* ptrColumn1 = &columns1;
    
    display1(ptrRow1, ptrColumn1);
    // Get elements to display as a whole after mat1 loop
    
    cout << "matrix2 # of rows: ";
    cin >> rows2;
    cout << "matrix2 # of columns: ";
    cin >> columns2;
    
    if(columns1>10 || rows1>10 || columns1<1 || rows1<1)
    return 0;
    
    if((rows2 != rows1) || (columns2 != columns1)){
    cout << "Operation is not supported";
    return 0;   
    }
 
    
    for(i=0;i<rows2;i++){
        for(j=0;j<columns2;j++){
            
            cout << "Enter element (" << i << "," << j << "): ";
            cin >> ev; // elemtent value
            mat2[i][j] = ev;
        }
        
    }
    
    int* ptrRow2 = &rows2;
    int* ptrColumn2 = &columns2;
    
    display2(ptrRow1, ptrColumn2);
    // Get elements to display as a whole after mat2 loop
    
      
    
    for(m=0;m<rows1;m++){
        for(n=0;n<columns1;n++){
            
            subMat[m][n] = mat1[m][n] - mat2[m][n];
            cout << subMat[m][n] << " ";
        }
        cout << endl;
    }
        
    main();
}


int multiplication(){
    
    int m, n, k=0, l=0, multMat[10][10] = {{0}};
    
      // Set bounds for matrix
    cout << "matrix1 # of rows: ";
    cin >> rows1;
    cout << "matrix1 # of columns: ";
    cin >> columns1;
    
    if(columns1>10 || rows1>10 || columns1<1 || rows1<1)
    return 0;
    
    
    
    for(i=0;i<rows1;i++){
        for(j=0;j<columns1;j++){
            
            cout << "Enter element (" << i << "," << j << "): ";
            cin >> ev; // elemtent value
            mat1[i][j] = ev;
        }
        
    }
    
    int* ptrRow1 = &rows1;
    int* ptrColumn1 = &columns1;
    
    display1(ptrRow1, ptrColumn1);
    // Get elements to display as a whole after mat1 loop
    
    cout << "matrix2 # of rows: ";
    cin >> rows2;
    cout << "matrix2 # of columns: ";
    cin >> columns2;
    
    if(columns1>10 || rows1>10 || columns1<1 || rows1<1)
    return 0;
    
   
    
    for(i=0;i<rows2;i++){
        for(j=0;j<columns2;j++){
            
            cout << "Enter element (" << i << "," << j << "): ";
            cin >> ev; // elemtent value
            mat2[i][j] = ev;
        }
        
    }
    
    int* ptrRow2 = &rows2;
    int* ptrColumn2 = &columns2;
    
    display2(ptrRow2, ptrColumn2);
    // Get elements to display as a whole after mat2 loop
    
    
    if(rows2 != columns1){
    cout << "Operation is not supported";
    return 0;   
    }
  
    
    
    for(m=0;m<rows1;m++){
        for(n=0;n<columns2;n++){
            for(k=0;k<columns1;k++){
                
            
           //multMat[m][n] = multMat[m][n] + mat1[m][k] * mat2[k][n];
           multMat[m][n] += mat1[m][k] * mat2[k][n];
           
            }
            
        }
    }
    for(m=0;m<rows1;m++){
                for(n=0;n<columns2;n++){
                    cout << multMat[m][n] << " ";
                    
                    }
                    cout << endl;
                    }
        main();
}


int determinant(){   // only one matrx, regulate inputs
    // 3x3 determinants
    int one, two, three, out;
    
      // Set bounds for matrix
    cout << "matrix1 # of rows: ";
    cin >> rows1;
    cout << "matrix1 # of columns: ";
    cin >> columns1;
    
    if(columns1>10 || rows1>10 || columns1<1 || rows1<1)
    return 0;
    
    
    
    for(i=0;i<rows1;i++){
        for(j=0;j<columns1;j++){
            
            cout << "Enter element (" << i << "," << j << "): ";
            cin >> ev; // elemtent value
            mat1[i][j] = ev;
        }
        
    }
    
    int* ptrRow1 = &rows1;
    int* ptrColumn1 = &columns1;
    
    display1(ptrRow1, ptrColumn1);
    // Get elements to display as a whole after mat1 loop
    

    
    if(rows1==columns1 && rows1 != 3){
        cout << "Operation is not supported for matrix 1";
    return 0;   // should return to menu
    }else{
        // mat1 determinant
        
        one = mat1[0][0] * ((mat1[1][1] * mat1[2][2]) - (mat1[1][2] * mat1[2][1]));
        two = mat1[0][1] * ((mat1[1][0] * mat1[2][2]) - (mat1[1][2] * mat1[2][0]));
        three = mat1[0][2] * ((mat1[1][0] * mat1[2][1]) - (mat1[1][1] * mat1[2][0]));
        out = one - two + three;
        cout << out << endl;
    }
   main();
}


int transpose(){
    
    int m, n, transMat[10][10];
    
    // Set bounds for matrix
    cout << "matrix1 # of rows: ";
    cin >> rows1;
    cout << "matrix1 # of columns: ";
    cin >> columns1;
    
    if(columns1>10 || rows1>10 || columns1<1 || rows1<1)
    return 0;
    
    for(i=0;i<rows1;i++){
        for(j=0;j<columns1;j++){
            
            cout << "Enter element (" << i << "," << j << "): ";
            cin >> ev; // elemtent value
            mat1[i][j] = ev;
        }
        
    }
    
    int* ptrRow1 = &rows1;
    int* ptrColumn1 = &columns1;
    
    display1(ptrRow1, ptrColumn1);
    
    for(i=0;i<columns1;i++){
        for(j=0;j<rows1;j++){
            
            
           cout << mat1[j][i] << " ";
        }
        cout << endl;
    }
    
    
    // Get elements to display as a whole after mat1 loop
    

    main();   // should return to menu
}

// only one matrx, regulate inputs
int inverse(){
    
    float m, n, a, b, c, d, e, f, g, h, z;
     float one, two, three, out;
     float inverseMat[10][10];
    
      // Set bounds for matrix
    cout << "matrix1 # of rows: ";
    cin >> rows1;
    cout << "matrix1 # of columns: ";
    cin >> columns1;
    
    if(columns1>10 || rows1>10 || columns1<1 || rows1<1)
    return 0;
    
    
    
    for(i=0;i<rows1;i++){
        for(j=0;j<columns1;j++){
            
            cout << "Enter element (" << i << "," << j << "): ";
            cin >> ev; // elemtent value
            mat1[i][j] = ev;
        }
        
    }
    
    int* ptrRow1 = &rows1;
    int* ptrColumn1 = &columns1;
    
    display1(ptrRow1, ptrColumn1);
    // Get elements to display as a whole after mat1 loop
    

    
    if(rows1==columns1 && rows1 != 3){
        cout << "Operation is not supported for matrix 1";
    return 0;   
    }else{
        // mat1 determinant
        
        one = mat1[0][0] * ((mat1[1][1] * mat1[2][2]) - (mat1[1][2] * mat1[2][1]));
        two = mat1[0][1] * ((mat1[1][0] * mat1[2][2]) - (mat1[1][2] * mat1[2][0]));
        three = mat1[0][2] * ((mat1[1][0] * mat1[2][1]) - (mat1[1][1] * mat1[2][0]));
        out = one - two + three;
        if(out == 0){
        cout << "Determinant is 0, therefore the inverse matrix does not exist.";
        return 0;
        }
        else{
            //  Transpose mini-det values
            a = (mat1[1][1] * mat1[2][2]) - (mat1[2][1] * mat1[1][2]);
            b = (mat1[0][1] * mat1[2][2]) - (mat1[2][1] * mat1[0][2]);
            c = (mat1[0][1] * mat1[1][2]) - (mat1[1][1] * mat1[0][2]);
            d = (mat1[1][0] * mat1[2][2]) - (mat1[2][0] * mat1[1][2]);
            e = (mat1[0][0] * mat1[2][2]) - (mat1[2][0] * mat1[0][2]);
            f = (mat1[0][0] * mat1[1][2]) - (mat1[1][0] * mat1[0][2]);
            g = (mat1[1][0] * mat1[2][1]) - (mat1[2][0] * mat1[1][1]);
            h = (mat1[0][0] * mat1[2][1]) - (mat1[2][0] * mat1[0][1]);
            z = (mat1[0][0] * mat1[1][1]) - (mat1[1][0] * mat1[0][1]);
            
           float adjM[3][3] = {{a, -b, c}, {-d, e, -f}, {g, -h, z}};   
          
            
            float recip = (1/out);
            
            // loop to output inverseMat
            
            for(i=0; i<rows1; i++){
                for(j=0; j<columns1; j++){
                    
                    inverseMat[i][j] = adjM[i][j] * recip;
                    cout << inverseMat[i][j] << " ";
                }
                cout << endl;
            }
            //  end
        }
    }
   
    
    main();   // should return to menu
}

void display1(int* rows1, int* columns1){
    
    int a, b;
    
    for(a=0;a<*rows1;a++){
        for(b=0;b<*columns1;b++){
            
            cout << mat1[a][b] << " ";
        }
        cout << endl;
    }
    cout << endl;
}


void display2(int* rows2, int* columns2){  
    
    int a, b;
    
    for(a=0;a<*rows2;a++){
        for(b=0;b<*columns2;b++){
            
            cout << mat2[a][b] << " ";
        }
        cout << endl;
    }
    cout << endl;
}
