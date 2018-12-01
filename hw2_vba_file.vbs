Attribute VB_Name = "Module1"
Sub TickerCounter()

Dim ws As Worksheet
Dim LastRow As Long
Dim Vol As Long
Dim VolCounter As Double

'run through each worksheet
For Each ws In Worksheets
    ws.Activate
    With ws
        Column = 1
        printcount = 2
          'run until last row in column A
          LastRow = .Cells(Rows.Count, "A").End(xlUp).Row
          
          'clear contents in column H were we want to fill in the unique values
          .Columns("H").ClearContents
          Range("A1:A" & LastRow).AdvancedFilter Action:=xlFilterCopy, CopyToRange:=Range("H1"), Unique:=True
    
          For i = 2 To LastRow
              
              Vol = Cells(i, 7).Value
              VolCounter = VolCounter + Vol
              
              'Searches for when the value of the next cell is different than that of the current cell
              If Cells(i + 1, Column).Value <> Cells(i, Column).Value Then
                      
                  'Print value in new cell
                  .Cells(1, 9) = "Total Stock Volume"
                  .Cells(printcount, 9).Value = VolCounter
                  printcount = printcount + 1
                      
                  'reset VolCounter
                  VolCounter = 0
              
              End If
             
          Next i
        
    End With
    
Next ws

End Sub


