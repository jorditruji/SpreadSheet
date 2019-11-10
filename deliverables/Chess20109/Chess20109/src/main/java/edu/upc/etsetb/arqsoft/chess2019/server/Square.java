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
public class Square {
    private Piece piece;
    private ArrayList<Integer> position; // col, row

    public Square( ArrayList<Integer> position) {
        this.piece = null;
        this.position = position;
    }


    
    public Piece getPiece() {
        return piece;
    }
    
    public Boolean isEmpty(){
        if(this.piece == null){
            return true;
        }
        else{
            return false;
        }
            
    }

 

    public void setPiece(Piece piece) {
        this.piece = piece;
    }

    public ArrayList<Integer> getPosition() {
        return position;
    }

    public void setPosition(ArrayList<Integer> position) {
        this.position = position;
    }
    
    
    
}
