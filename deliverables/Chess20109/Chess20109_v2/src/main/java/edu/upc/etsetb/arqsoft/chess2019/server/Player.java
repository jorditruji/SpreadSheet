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
        
        //PEONS
        Integer row = this.color==Color.BLACK ? 2: 7; 
        for (int i = 1; i<=8; i++){
            Piece piece = new PiecePawn("P",this.color);
            ArrayList<Integer> position = new ArrayList<Integer>();
            position.add(i);
            position.add(row);
            // For board initialization null is given to positionOrigin
            this.putPiece(piece, board, position, null);
        }
        
        // ROCKS
        ArrayList<Integer> cols = new ArrayList<Integer>();
        cols.add(1);
        cols.add(8);
        row = this.color==Color.BLACK ? 1: 8;
        for (int i = 0; i < 2; i++) {
            Piece piece = new PieceRook("R", this.color);
            ArrayList<Integer> position = new ArrayList<Integer>();
            position.add(cols.get(i));
            position.add(row);
            // For board initialization null is given to positionOrigin
            this.putPiece(piece, board, position, null);
        }
        
        // KNIGTS
        cols = new ArrayList<Integer>();
        cols.add(2);
        cols.add(7);
        row = this.color==Color.BLACK ? 1: 8;
        for (int i = 0; i < 2; i++) {
            Piece piece = new PieceKnight("N", this.color);
            ArrayList<Integer> position = new ArrayList<Integer>();
            position.add(cols.get(i));
            position.add(row);
            // For board initialization null is given to positionOrigin
            this.putPiece(piece, board, position, null);
        }
        
        //BISHOPS
        cols = new ArrayList<Integer>();
        cols.add(3);
        cols.add(6);
        row = this.color==Color.BLACK ? 1: 8;
        for (int i = 0; i < 2; i++) {
            Piece piece = new PieceBishop("B", this.color);
            ArrayList<Integer> position = new ArrayList<Integer>();
            position.add(cols.get(i));
            position.add(row);
            // For board initialization null is given to positionOrigin
            this.putPiece(piece, board, position, null);
        }
        
        //KING
        Piece piece = new PieceKing("K", this.color);
        row = this.color==Color.BLACK ? 1: 8;
        ArrayList<Integer> position = new ArrayList<Integer>();
        position.add(5);
        position.add(row);
        // For board initialization null is given to positionOrigin
        this.putPiece(piece, board, position, null);
        
        // QUEEN
        piece = new PieceQueen("Q", this.color);
        row = this.color==Color.BLACK ? 1: 8;
        position = new ArrayList<Integer>();
        position.add(4);
        position.add(row);
        
        
    }
    
    public void putPiece(Piece piece, Board board, ArrayList<Integer> positionDestination, ArrayList<Integer> positionOrigin) {
        board.setPiece(piece, positionDestination, positionOrigin);
        
    }
    
    public String move(int rO, int cO, int rD, int cD, Board b ){
        ArrayList<Integer> positionOrigin = new ArrayList<Integer>();
        positionOrigin.add(cO);
        positionOrigin.add(rO);
        Piece piece = b.getSquare(positionOrigin).getPiece();
        String message = piece.canReachDestination(rO, cO, rD, cD, b);
        return message;
    }
    
}
