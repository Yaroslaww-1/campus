FROM mcr.microsoft.com/dotnet/sdk:5.0 AS builder
WORKDIR /app

COPY Users.csproj ./
RUN dotnet restore Users.csproj

COPY . ./source/
WORKDIR /app/source
RUN dotnet publish -c release -o /release

FROM mcr.microsoft.com/dotnet/aspnet:5.0
WORKDIR /release
COPY --from=builder /release ./
ENTRYPOINT ["dotnet", "Users.dll"]