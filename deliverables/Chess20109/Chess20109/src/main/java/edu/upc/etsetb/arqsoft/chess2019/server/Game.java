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
public class Game {
        protected ArrayList<Player> players;
        protected Board board;

//    

    public Game() {
        this.players = new  ArrayList<Player>();
        this.board = new Board();
        
      
        for (Color color : Color.values()) { 
        
            Player player = new Player(color);
            this.players.add(player);
            
        }
            
    

    }

    public Board getBoard() {
        return board;
    }

    public void setBoard(Board board) {
        this.board = board;
    }

    public ArrayList<Player> getPlayers() {
        return players;
    }

    public void setPlayers(ArrayList<Player> players) {
        this.players = players;
    }
}
