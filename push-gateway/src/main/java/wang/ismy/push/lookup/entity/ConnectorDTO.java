package wang.ismy.push.lookup.entity;

import lombok.Data;
import lombok.EqualsAndHashCode;

@Data
@EqualsAndHashCode
public class ConnectorDTO {
    private String host;
    private Integer port;
    private String area;

    public static ConnectorDTO emptyConnector(){
        ConnectorDTO connector = new ConnectorDTO();
        connector.setArea("default");
        connector.setHost("");
        connector.setPort(-1);
        return connector;
    }
}
