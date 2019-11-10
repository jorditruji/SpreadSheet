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
public class Player {
    protected Color color;

    public void setColor(Color color) {
        this.color = color;
    }

    public Color getColor() {
        return color;
    }

    public Player(Color color, Board board) {
        this.color = color;
        for (int i = 1; i<=8; i++){
            Piece peo = new Piece("P",this.color);
            ArrayList<Integer> position = new ArrayList<Integer>();
            Integer row = this.color==Color.BLACK ? 2: 7; 
            position.add(i);
            position.add(row);
            // For board initialization null is given to positionOrigin
            this.putPiece(peo, board, position, null);
        }
    }
    
    public void putPiece(Piece piece, Board board, ArrayList<Integer> positionDestination, ArrayList<Integer> positionOrigin) {
        board.setPiece(piece, positionDestination, positionOrigin);
        
    }
    
}
