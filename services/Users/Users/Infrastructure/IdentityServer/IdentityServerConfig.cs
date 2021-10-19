using System.Collections.Generic;
using IdentityServer4;
using IdentityServer4.Models;

namespace Users.Infrastructure.IdentityServer
{
	public class IdentityServerConfig
	{
		public static IEnumerable<ApiResource> GetApis()
		{
			return new List<ApiResource>
			{
				new ApiResource("UsersAPI", "Users API")
			};
		}

		public static IEnumerable<IdentityResource> GetIdentityResources()
		{
			return new IdentityResource[]
			{
				new IdentityResources.OpenId(),
				new IdentityResources.Profile(),
				new IdentityResource(CustomClaimTypes.Roles, new List<string>
				{
					CustomClaimTypes.Roles
				}),
			};
		}

		public static IEnumerable<Client> GetClients()
		{
			return new List<Client>
			{
				new Client
				{
					ClientId = "ro.client",
					AllowedGrantTypes = GrantTypes.ResourceOwnerPassword,
					AllowOfflineAccess = true,
					AccessTokenLifetime = 300,
					SlidingRefreshTokenLifetime = 3600,
					RefreshTokenUsage = TokenUsage.OneTimeOnly,
					RefreshTokenExpiration = TokenExpiration.Sliding,
					ClientSecrets =
					{
						new Secret("secret".Sha256())
					},
					AllowedScopes =
					{
						"UsersAPI",
						IdentityServerConstants.StandardScopes.OpenId,
						IdentityServerConstants.StandardScopes.Profile
					}
				}
			};
		}
	}
}
