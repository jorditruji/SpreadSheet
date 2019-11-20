/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package edu.upc.etsetb.arqsoft.chess2019.server;

/**
 *
 * @author jordi
 */
public abstract class Piece {
    private String figure;
    private Color color;

    public Piece(String figure, Color color) {
        this.color = color;
        if(color==Color.BLACK){
            this.figure = "B"+figure ;
        }else{
            this.figure = "W"+figure ;
        }
    }

    public Color getColor() {
        return color;
    }

    public String getFigure() {
        return figure;
    }

    public void setFigure(String figure) {
        this.figure = figure;
    }
    
    
    public abstract boolean isPieceMovement(int rO, int cO, int rD, int cD) throws NoPieceMovementException;
    public abstract boolean isPathFree(int rO, int cO, int rD, int cD, Board board) throws NoPathFreeException;

    public String canReachDestination(int rO, int cO, int rD, int cD, Board b) 
    {
        String message = "";
        try{
           boolean isValidMovement = this.isPieceMovement(rO, cO, rD, cD);
           if (!isValidMovement)
           {
                message = "E The requested movement is not valid for the piece.";
   
           }else{
               try{
                    boolean isPathFree = this.isPathFree(rO, cO, rD, cD, b);
                    if (!isPathFree){
                        message = "E The requested path is not free for the piece.";
                    }
               }catch(NoPathFreeException e){
                   message = "E Failed to check the path";
               }
           }        
        }
        catch(NoPieceMovementException e ){
            message = "E Failed to evaluate movement";

        }
        return message;
    }

    public static class NoPieceMovementException extends Exception {

        public NoPieceMovementException() {
        }
    }

    public static class NoPathFreeException extends Exception {

        public NoPathFreeException() {
        }
    }

}
