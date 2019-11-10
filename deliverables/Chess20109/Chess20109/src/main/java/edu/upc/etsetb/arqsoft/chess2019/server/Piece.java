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
public class Piece {
    private String figure;

    public Piece(String figure, Color color) {
        if(color==Color.BLACK){
            this.figure = "B"+figure ;
        }else{
            this.figure = "W"+figure ;
        }
    }

    public String getFigure() {
        return figure;
    }

    public void setFigure(String figure) {
        this.figure = figure;
    }
    

   
    
}
