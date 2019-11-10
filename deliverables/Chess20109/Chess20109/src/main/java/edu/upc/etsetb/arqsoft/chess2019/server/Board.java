/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package edu.upc.etsetb.arqsoft.chess2019.server;

import java.util.ArrayList;

/**
 *
 * @author jordi
 */
public class Board {
    private ArrayList<Square> squares;

    public Board() {
        this.squares = new ArrayList<Square>();
        // For 64 squares crate empty square
        for (int i=1;i<=8;i++){
            for (int j=1; j<=8;j++){
                ArrayList<Integer> position = new ArrayList<Integer>();
                position.add(i);
                position.add(j);
                this.squares.add(new Square(position));
                
            }
        }
        

    }
    public Square getSquare(ArrayList<Integer> position){
        Square result = new Square(position);
        for(Square square: this.squares){
            if(square.getPosition().equals(position)){
                result =  square;
            }
            
        }
        return result;
    }
    public void setPiece(Piece piece, ArrayList<Integer> position){
        this.getSquare(position).setPiece(piece);
        
    }

    
    
    
}
