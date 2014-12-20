package storing;

import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;


public class StoringInterface{

	
	//conexion con la base de datos

	//se llama al método de la base de datos que guarda el voto

	public static void saveVote(String vote, Integer votacionId) {
		try{
			DbConnection conex= new DbConnection();
			PreparedStatement consulta = conex.getConnection().prepareStatement("INSERT INTO `Votes` (`votacion_id`,`vote`) VALUES (?,?)");
			consulta.setInt(1, votacionId);
			consulta.setString(2, vote);
			consulta.execute();
			conex.desconectar();	
		}catch(SQLException e){
			System.out.println("Se ha producido un error al guardar los votos.");
		}
	}
	
	//se llama al método de la base de datos que devuelve todos los votos

	public static ResultSet findAllVotes(Integer votacionId) {
		ResultSet res = null;
		try{
			DbConnection conex= new DbConnection();
			PreparedStatement consulta = conex.getConnection().prepareStatement("SELECT * FROM Votes where votacion_id = ?");
			consulta.setInt(1, votacionId);
			res = consulta.executeQuery();
			conex.desconectar();	
		}catch(SQLException e){
			System.out.println("Se ha producido un error al buscar los votos.");
		}
		return res;
	}

	
}
