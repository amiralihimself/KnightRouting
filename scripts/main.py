from chessboard import chessBoard
import search_algorithms as searchAlgos

if __name__ == "__main__":
     dimension=20
     squareSize=30
     screenHeight=600
     screenWidth=800
     overHeadText="Knight Routing by Amirali"
     c1=chessBoard(dimension,squareSize, screenHeight,screenWidth)
     c1.drawBoard(overHeadText)
     c1.setBarriers()
     srcRow, srcCol, desRow, desCol, boardArray= c1.setSourceAndDestination()
     visitedAlongTheWay=[]
