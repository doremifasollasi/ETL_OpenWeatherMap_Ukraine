SELECT local_net_address
FROM sys.dm_exec_connections
WHERE session_id = @@SPID

-- If NULL, then
-- environment:
--   SQL_SERVER: host.docker.internal
 